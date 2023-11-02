def solution():
    """Doctor Jones is scheduling his time for Monday. He is spending nine hours at the clinic where he works that day. He has to do rounds to check on inpatients staying at the clinic, which takes twenty minutes per inpatient, and he has ten appointments, which take thirty minutes each. How many hours will Doctor Jones have left to update his records if he has 9 inpatients at the clinic?"""
    clinic_hours = 9
    inpatients = 9
    inpatient_time = inpatients * 20 / 60  # converting minutes to hours
    appointment_time = 10 * 30 / 60  # converting minutes to hours
    total_time = inpatient_time + appointment_time
    remaining_time = clinic_hours - total_time
    result = remaining_time
    return result

print(solution())