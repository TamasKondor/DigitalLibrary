class User:    
    
    def __init__(self, userid, fname, lname, added, role, accname, pwd):
        self.userid = userid
        self.fname = fname
        self.lname = lname
        self.added = added
        self.role = role
        self.accname = accname
        self.pwd = pwd
     
    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def getListItem(self ):
        return '{0:2} {1:<12} {2:<10} {3:<10}'.format(self.userid, self.fullname, self.added, self.role)

class Users(User):

    def __init__(self, dict_list):        
        self.userList = []
        for item in dict_list:
            self.userList.append(User(item["User_id"], item["FName"], item["LName"], item["Added"], item["Role"], item["AccName"], item["Passwd"]))

    def getUserList(self):
        return self.userList

    def getUserByAccount(self, AName):
        for itm in self.userList:
           if itm.accname == AName:
              return itm
        return None



class Content:    
    
    def __init__(self, contentid, typeid, name, author, stock, available, price, active):
        self.contentid = contentid
        self.typeid = typeid
        self.name = name
        self.author = author
        self.stock = stock
        self.available = available
        self.price = price
        self.active = active
     
    def getListItem(self):
        list_contForm = []
        list_contForm.append('{0:<35} {1:<23} {2:<2}'.format( "Name", "Author", "In"))
        return '{0:<35} {1:<23} {2:<2}'.format( self.name, self.author, self.available)

class Contents(Content):        

    def __init__(self, dict_list):        
        self.contentList = []
        for item in dict_list:
            self.contentList.append(Content(item["Content_id"], item["Type_id"], item["Name"], item["Author"], item["Stock"], item["Available"], item["Price"], item["Active"]))

    def getContentList(self):
        return self.contentList

    def getContentByType(self, TypeId):
        defTypeList = []
        for itm in self.contentList:
           if itm.typeid == TypeId:
              defTypeList.append(itm)              
        return defTypeList

class ContType:    
    
    def __init__(self, typeid, typename):
        self.typeid = typeid
        self.typename = typename        
     
    def getListItem(self ):
        return '{0:2} {1:<20}'.format(self.typeid, self.typename)

class ContTypes(ContType):
    
    def __init__(self, dict_list):        
        self.typeList = []
        for item in dict_list:
            self.typeList.append(ContType(item["Type_id"], item["TypeName"]))

    def getTypeList(self):
        return self.typeList

    def geTypeById(self, type_id):
        for itm in self.typeList:
           if itm.typeid == type_id:
              return itm.typename
        return None

    def getIdByType(self, type_name):
        for itm in self.typeList:
           if itm.typename == type_name:
              return itm.typeid
        return None
    
 



# usr1 = User(1, "Test", "Elek", "2020-10-21", "user", 'telek', 't')
# print(usr1.fullname)
# print(usr1.getListItem())

# cont1 = Content(1, 1, "Oracle Database 10g", "Kevin Loney", 10, 10, 1.95, 1)
# print(cont1.getListItem())

# type1 = ContType(1, "eBook")
# print(type1.getListItem())


    
