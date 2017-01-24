#
# Custom AWS Config Rule - Skeleton Code
#

import boto3, json

def evaluate_compliance(config_item, vpc_id):
    return 'NON_COMPLIANT'

def lambda_handler(event, context):
    
    # Create AWS SDK clients & initialize custom rule parameters
    config = boto3.client('config')
    invoking_event = json.loads(event['invokingEvent'])
    compliance_value = 'NOT_APPLICABLE'
    resource_id = invoking_event['configurationItem']['resourceId']
                
    
    compliance_value = evaluate_compliance(invoking_event['configurationItem'], resource_id)
          
    
    response = config.put_evaluations(
       Evaluations=[
            {
                'ComplianceResourceType': invoking_event['configurationItem']['resourceType'],
                'ComplianceResourceId': resource_id,
                'ComplianceType': compliance_value,
                'Annotation': 'Insert text here to detail why control passed/failed',
                'OrderingTimestamp': invoking_event['notificationCreationTime']
            },
       ],
       ResultToken=event['resultToken'])