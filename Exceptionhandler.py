class Exception:
    def get_userexception(self,id):
        return "ID :"+id+" does not exists in the table"
        
    def getalluserexception(self,tablename):
        return "Table :"+tablename+" not found in the database"