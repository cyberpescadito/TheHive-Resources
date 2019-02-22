import json
from thehive_hooks import app
from thehive_hooks import ee
from thehive4py.api import TheHiveApi

api = TheHiveApi('http://myhive.com', 'My API Key', cert=False)

def make_handler_func(event_name):
    @ee.on(event_name)
    def _handler(event):
        app.logger.info('Handle {}: Event={}'.format(event_name, json.dumps(event, indent=4, sort_keys=True)))

    return _handler

def defineRegionFromTLA(TLASan):
        regionAmerica = ['NYC', 'WDC', 'LAS', 'SAN']
        regionAP = ['SYD', 'TKY', 'SGP']
        regionEU = ['PAR', 'BER', 'MAD']
        if TLASan in regionAmerica:
                Region='America'
        elif TLASan in regionEU:
                Region='EU'
        elif TLASan in regionAP:
                Region='AP'
        else:
                Region = 'To Complete'
        return Region

events = [
    'AlertCreation',
    'AlertUpdate',
    'CaseArtifactCreation',
    'CaseArtifactJobCreation',
    'CaseArtifactJobUpdate',
    'CaseArtifactJobUpdate',
    'CaseArtifactUpdate',
    'CaseCreation',
    'CaseTaskCreation',
    'CaseTaskLogCreation',
    'CaseTaskUpdate',
    'CaseUpdate'
]

for e in events:
    make_handler_func(e)

@ee.on('CaseUpdate')
def updatedTLA(event):
        noAction = 0
        if 'Region' in event['details']['customFields']:
                noAction = 1
                #The previous action avoid loops & allow analyst to change manually the region without risk of triggering the webhook
        if 'TLA' in event['details']['customFields'] and noAction == 0:
                TLA = (event['details']['customFields']['TLA'])
                TLASan = TLA['string']
                Region = defineRegionFromTLA(TLASan)
                RegionFinal = {"string":Region,"order":9}
                hiveCase = api.case(event['objectId'])
                hiveCase.customFields['Region'] = RegionFinal
                api.update_case(hiveCase, ['customFields'])
