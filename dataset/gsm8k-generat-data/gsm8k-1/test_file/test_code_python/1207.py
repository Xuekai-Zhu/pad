def solution():
    """For one medical dosage, Saanvi had to combine 14 mL of one medicine with 3 times that amount of the second medicine. How many mL of medicine would be in 8 doses?"""
    medicine1 = 14
    medicine2 = medicine1 * 3
    total_medicine = medicine1 + medicine2
    doses = 8
    total_medicine *= doses
    result = total_medicine
    return result

print(solution())