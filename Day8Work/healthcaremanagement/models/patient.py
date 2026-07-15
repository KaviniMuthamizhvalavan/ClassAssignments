from models.person import Person

class Patient(Person):
    def __init__(self, id, name, age, ailment):
        super().__init__(id, name, age)  #reusability of code from Person class
        self.ailment = ailment

    def get_details(self):
        details = super().get_details()   # inherit base details
        details.update({"ailment": self.ailment})
        return details
    
    def display_info(self):
        return f"{super().display_info()}, Ailment: {self.ailment}"