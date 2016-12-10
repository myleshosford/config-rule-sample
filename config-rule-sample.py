#
# Sample config rule framework code
#

import boto3, json

def lambda_handler(event, context):
    
    #Create AWS clients
    #iam = boto3.client('iam')
    config = boto3.client('config')
    
    #Create current invokation info
    invoking_event = json.loads(event['invokingEvent'])
    compliance_value = 'NOT_APPLICABLE'
    account_id = event['accountId']
                
    #Evaluate Compliance
    if (1 < 2):
        compliance_value = 'NON_COMPLIANT'
    else:
        compliance_value = 'COMPLIANT'
        
    
    response = config.put_evaluations(
       Evaluations=[
            {
                'ComplianceResourceType': 'AWS::::Account',
                'ComplianceResourceId': account_id,
                'ComplianceType': compliance_value,
                'Annotation': 'Insert text here to detail why control passed/failed',
                'OrderingTimestamp': invoking_event['notificationCreationTime']
            },
       ],
       ResultToken=event['resultToken'])