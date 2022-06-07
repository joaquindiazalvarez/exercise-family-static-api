
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    
    
    def __init__(self, last_name):
        self.last_name = last_name   # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "lucky_numbers": [7, 13, 22],
            "age": 33
            },{
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "lucky_numbers": [10, 14, 3],
            "age": 35
             },{
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "lucky_numbers": [1],
            "age": 5
            }]
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member_list = self._members
        member_out = {
            "id": self._generateId(),
            "first_name": member['first_name'],
            "last_name": self.last_name,
            "lucky_numbers": member['lucky_numbers'],
            "age": member['age']
            }
        if "id" in member:
            member_out['id'] = member['id']
        member_list.append(member_out)
        self._members = member_list
        return member_out

    def delete_member(self, id):
        members = self._members
        for i in range(len(members)):
            if members[i]['id'] == id:
                index = i
        members.pop(index)
        self._members = members
        return members

    def get_member(self, member_id):
        members = self._members
        for element in members:
            if element['id'] == member_id:
                return element
        return "not found"

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
