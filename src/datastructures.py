
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
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if member.get("id") is None:
            member["id"] = self._generateId()
        
        self._members.append({
            "id": member["id"],
            "first_name": member["first_name"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        })

    def delete_member(self, id):
        self._members = [elem for elem in self._members if elem["id"] != id]
        return self._members

    def get_member(self, id):
        #sigle_member = [elem for elem in self._members if elem["id"] == id]
        #return single_member[0] if single_member else None
        return next((elem for elem in self._members if elem["id"] == id), None)

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
