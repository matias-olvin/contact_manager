from manager import Manager
from pymongo import ASCENDING, MongoClient
from pymongo.errors import DuplicateKeyError


class ContactManager(Manager):
    def __init__(self, list_name: str) -> None:
        self.list_name = list_name

        self.client = MongoClient(host="localhost", port=27017)

        self.db = self.client["contacts"]

        self.document = self.db[f"{list_name}_storage"]

    def add_contact(self, name: str, phone_number: str, email: str, **kwargs):
        basic_details = {"name": name, "phone_number": phone_number, "email": email}

        full_contact_details = {**basic_details, **kwargs}

        self._add_contact_to_db(full_contact_details)

    # def remove_contact(self, name: str):
    #     client = MongoClient(host="localhost", port=27017)

    #     db[]

    def _add_contact_to_db(self, storage_item: dict):
        name = storage_item["name"]

        self.document.create_index([("name", ASCENDING)], unique=True)
        try:
            self.document.insert_one(storage_item)

            print(f"Added {name} to {self.list_name}")
        except DuplicateKeyError:
            print(f"{name} already exists in {self.list_name}")

        self.client.close()


phone_book = ContactManager("matty_phonebook")

phone_book.add_contact(
    name="Andy Sanchez",
    phone_number="01234714960",
    email="andy@gmail.com",
    guardian_name="Xanthe",
    guardian_relationship="Mother",
)
