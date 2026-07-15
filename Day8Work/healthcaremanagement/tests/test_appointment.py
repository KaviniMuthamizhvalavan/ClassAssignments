from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from services.healthcare_system import HealthcareSystem

def test_appointment_linking_and_retrieval():
    datastore = {"patients": {}, "doctors": {}, "appointments": {}} 
    system = HealthcareSystem(datastore)
    
    system.patient_service.add_patient(Patient(1, "John Doe", 30, "Flu"))
    system.doctor_service.add_doctor(Doctor(101, "Dr. Alice", 45, "General"))
    
    app = Appointment(1001, 1, 101, "2026-07-20", "10:00 AM")
    system.appointment_service.create_appointment(app) 
    
    info = system.appointment_service.get_appointment(1001)
    assert info is not None
    assert "Patient ID: 1" in info
    assert "Doctor ID: 101" in info
    assert "Date: 2026-07-20" in info

def test_appointment_update_and_delete():
    datastore = {"patients": {}, "doctors": {}, "appointments": {}} 
    system = HealthcareSystem(datastore)
    
    system.patient_service.add_patient(Patient(1, "John Doe", 30, "Flu"))
    system.doctor_service.add_doctor(Doctor(101, "Dr. Alice", 45, "General"))
    
    app = Appointment(1001, 1, 101, "2026-07-20", "10:00 AM")
    system.appointment_service.create_appointment(app) 
    
    system.appointment_service.update_appointment(1001, time="11:30 AM")
    assert datastore["appointments"][1001].time == "11:30 AM"
    
    system.appointment_service.delete_appointment(1001)
    assert system.appointment_service.get_appointment(1001) is None