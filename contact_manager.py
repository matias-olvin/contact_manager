from pymongo import ASCENDING, MongoClient
from pymongo.errors import DuplicateKeyError

from manager import Manager


class ContactManager(Manager):
    def __init__(self, list_name: str) -> None:
        self.list_name = list_name
        self.document_name = f"{list_name.strip().lower().replace(' ', '_')}_storage"
        self.db_name = "contacts"

        client = MongoClient(host="localhost", port=27017)
        db = client[self.db_name]
        document = db[self.document_name]

        document.create_index([("name", ASCENDING)], unique=True)

        client.close()

    def add_contact(self, name: str, phone_number: str, email: str, **kwargs):
        basic_details = {"name": name, "phone_number": phone_number, "email": email}

        full_contact_details = {**basic_details, **kwargs}

        self._add_contact_to_db(full_contact_details)

    def find_contact(self, search_value: str, find_by: str = "name"):
        client = MongoClient(host="localhost", port=27017)
        db = client[self.db_name]
        document = db[self.document_name]

        cursor = document.find({find_by: search_value})

        for item in cursor:
            print(item)

        client.close()

    def _add_contact_to_db(self, storage_item: dict):
        name = storage_item["name"]

        client = MongoClient(host="localhost", port=27017)
        db = client[self.db_name]
        document = db[self.document_name]

        try:
            document.insert_one(storage_item)

            print(f"Added {name} to {self.list_name}")
        except DuplicateKeyError:
            print(f"{name} already exists in {self.list_name}")

        client.close()
