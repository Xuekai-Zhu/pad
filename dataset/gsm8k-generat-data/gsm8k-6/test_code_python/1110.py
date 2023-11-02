def solution():
    # Calculate the total amount of medicine needed for the child
    total_medicine = 30 * 5  # for every kilogram of weight, the child must be given 5 ml of medicine
    
    # Calculate the amount of medicine needed for each dose
    single_dose = total_medicine / 3
    
    result = single_dose
    return result

print(solution())