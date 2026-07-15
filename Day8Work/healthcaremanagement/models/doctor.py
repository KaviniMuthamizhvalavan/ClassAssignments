from models.person import Person

class Doctor(Person):
    def __init__(self, id, name, age, specialization):
        super().__init__(id, name, age)   
        self.specialization = specialization 

    def get_details(self):
        details = super().get_details()  
        details.update({"specialization": self.specialization})
        return details

    def display_info(self):
        return f"{super().display_info()}, Specialization: {self.specialization}"