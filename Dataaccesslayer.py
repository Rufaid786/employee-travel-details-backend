import boto3
class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')

    def put_item(self,table_name,data):
        # Insert an item into the given DynamoDB table
        item={'id':data['id'],'Account': data['account'],'Project/Contract': data['project'],'Emp ID': data['empid'],'Emp Name': data['empname'],'Purpose of Travel': data['purposeoftravel'],'Travel from': data['travelfrom'],'Travel to':data['travelto'],'Date from':data['datefrom'],'Date To':data['dateto'],'Flight':data['flight'],'Hotac':data['hotac'],'Perdiem':data['perdiem'],'Other cost':data['othercost'],'Total Cost':data['totalcost'],'Comments if Any':data['commentsifany']}
        self.dynamodb.Table(table_name).put_item(Item=item)

    def getitem(self, table_name,empid):
        # Retrieve an item from the given DynamoDB table by its primary key
        response = self.dynamodb.Table(table_name).get_item(Key={'id':empid})
        req=response['Item']
        return req
    
   
    def scan(self, table_name):
        # Retrieve all items from the given DynamoDB table
        response = self.dynamodb.Table(table_name).scan()
        return response['Items']