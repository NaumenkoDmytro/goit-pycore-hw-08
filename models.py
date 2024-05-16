from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
		pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("The number is not valid!")
        super().__init__(value)
        self.value = value


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

                             
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_birthday(self, value):
        self.birthday = Birthday(value)
    

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    

    def remove_phone(self, rem_phone):
        for phone in self.phones:
            if phone.value == rem_phone:
                self.phones.remove(phone)
           
    
    def edit_phone(self, old_phone, edited_phone):
        for idx, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[idx] = Phone(edited_phone)
                break
        else:
            raise ValueError ('This number does not exist')
                

    def find_phone(self, current_phone):
        for phone in self.phones:
            if phone.value == current_phone:
                return phone
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):


    def add_record(self,record):
        self.data[record.name.value] = record
           

    def find(self, name):
        return self.data.get(name)
           
    
    def delete(self,name):
        if name not in self.data:
            raise KeyError ('Name not found')
        else:
            del self.data[name]

    
    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today().date()

        for record in self.data.values():
            if record.birthday:
                user_birthday = record.birthday.value
                next_birthday = user_birthday.replace(year=today.year) 
            if next_birthday < today:
                next_birthday = user_birthday.replace(year=today.year+1)
            if (next_birthday - today).days <= 7:
                upcoming_birthdays.append({"name": record.name.value, "birthday": next_birthday.strftime("%d.%m.%Y") })
        
        return upcoming_birthdays