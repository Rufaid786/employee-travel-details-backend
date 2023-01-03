from Dataaccesslayer import DynamoDB
from Exceptionhandler import Exception

#creating an object of dynamodb in order to interact with data accesslayer
dynamodb = DynamoDB()
exception=Exception()
class UserManager:

    def add_user(self,tablename,value):
        # validate the user input
        # perform any other business logic tasks
        # insert the user into the DynamoDB table using the data access layer
        dynamodb.put_item(table_name=tablename,data=value)

    def get_user(self,tablename,parameter):
        # retrieve a user from the DynamoDB table by its primary key using the data access layer
        try:
            user = dynamodb.getitem(table_name=tablename, empid=parameter['id'])
            return user
        except:
            error=exception.get_userexception(parameter['id'])
            return error
            
            
    def getall_users(self,tablename):
        try:
            #return dynamodb.findtable(tablename)
            return dynamodb.scan(tablename)
        except:
            return exception.getalluserexception(tablename)
            