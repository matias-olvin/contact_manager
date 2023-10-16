from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def add_contact(self):
        pass

    # @abstractmethod
    # def remove_contact(self):
    #     pass

    # @abstractmethod
    # def search_for_contact(self):
    #     pass

    # @abstractmethod
    # def edit_contact(self):
    #     pass

    # @abstractmethod
    # def _add_contact_to_db(self):
    #     pass