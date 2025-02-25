from typing import List
from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Awesomeobject:
   SomeProps1: int
   SomeProps2: str

   @staticmethod
   def from_dict(obj: Any) -> 'Awesomeobject':
        _SomeProps1 = int(obj.get("SomeProps1"))
        _SomeProps2 = str(obj.get("SomeProps2"))
        return Awesomeobject(_SomeProps1, _SomeProps2)

@dataclass
class User:
   id: str
   name: str
   created_at: str
   updated_at: str
   email: str
   testanadditionalfield: str

   @staticmethod
   def from_dict(obj: Any) -> 'User':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        _created_at = str(obj.get("created_at"))
        _updated_at = str(obj.get("updated_at"))
        _email = str(obj.get("email"))
        _testanadditionalfield = str(obj.get("testanadditionalfield"))
        return User(_id, _name, _created_at, _updated_at, _email, _testanadditionalfield)

@dataclass
class Class1:
   id: int
   user_id: str
   awesomeobject: Awesomeobject
   created_at: str
   updated_at: str
   users: List[User]

   @staticmethod
   def from_dict(obj: Any) -> 'Class1':
        _id = int(obj.get("id"))
        _user_id = str(obj.get("user_id"))
        _awesomeobject = Awesomeobject.from_dict(obj.get("awesomeobject"))
        _created_at = str(obj.get("created_at"))
        _updated_at = str(obj.get("updated_at"))
        _users = [User.from_dict(y) for y in obj.get("users")]
        return Class1(_id, _user_id, _awesomeobject, _created_at, _updated_at, _users)

@dataclass
class Class2:
   SomePropertyOfClass2: str

   @staticmethod
   def from_dict(obj: Any) -> 'Class2':
        _SomePropertyOfClass2 = str(obj.get("SomePropertyOfClass2"))
        return Class2(_SomePropertyOfClass2)

@dataclass
class Root:
   Class1: Class1
   Class2: Class2

   @staticmethod
   def from_dict(obj: Any) -> 'Root':
        _Class1 = Class1.from_dict(obj.get("Class1"))
        _Class2 = Class2.from_dict(obj.get("Class2"))
        return Root(_Class1, _Class2)

# Example Usage
jsonstring = json.loads(myjsonstring)
root = Root.from_dict(jsonstring)

output = json.load(open('data.json'))
result = Root.from_dict(output)
test = result.Class1.awesomeobject.SomeProps1
test2 = result.Class1.users[0].email
test3 = 2
