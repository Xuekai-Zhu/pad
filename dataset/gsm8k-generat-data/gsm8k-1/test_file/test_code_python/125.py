def solution():
    """A hospital sees 500 people a day. Each patient is seen for an average of 24 minutes. The doctors charge $150 an hour to the hospital and the hospital charges the patients $200 an hour. How much profit does the hospital make from these visits?"""
    patients_per_day = 500
    minutes_per_patient = 24
    hours_per_patient = minutes_per_patient / 60
    doctor_fee_per_hour = 150
    hospital_charge_per_hour = 200
    doctor_fee_per_patient = doctor_fee_per_hour * hours_per_patient
    hospital_profit_per_patient = hospital_charge_per_hour - doctor_fee_per_hour
    total_profit_per_day = patients_per_day * hospital_profit_per_patient
    result = total_profit_per_day
    return result

print(solution())