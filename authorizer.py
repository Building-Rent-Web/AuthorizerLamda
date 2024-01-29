import jwt
def handler(event, context):
    
    token = event["headers"]["Authorization"]
    
    try:
        decoded = jwt.decode(token, '123456', algorithms=['HS256'])
        principalId = decoded['sub']
        
        if "@columbia.edu" in principalId:
            policyDocument = {
                'Version': '2012-10-17',
                'Statement':[{
                    'Action': 'execute-api:Invoke',
                    'Effect':'Allow',
                    'Resource': event['methodArn']
                }]
            }
        else:
            principalId = 'unauthorized'
            policyDocument = {
                'Version': 2012-10-17,
                'Statement':[{
                    'Action': 'execute-api:Invoke',
                    'Effect':'Deny',
                    'Resource': event['methodArn']
                }]
            }            
    except:
        principalId = 'unauthorized'
        policyDocument = {
            'Version': 2012-10-17,
            'Statement':[{
                'Action': 'execute-api:Invoke',
                'Effect':'Deny',
                'Resource': event['methodArn']
            }]
        }
        
        
    return {
        'principalId': principalId,
        'policyDocument': policyDocument,
         "context": {
            "email": principalId,
          }
    }
