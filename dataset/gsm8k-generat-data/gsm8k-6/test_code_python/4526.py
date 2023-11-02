def solution():
    # Calculate the total cost of the vaccinations and doctor's visit
    medical_cost = (10 * 45) + 250  # 10 vaccines cost $45 each and the doctor's visit costs $250
    medical_cost_after_insurance = medical_cost * 0.2  # insurance covers 80% of the medical bills
    total_cost = medical_cost_after_insurance + 1200  # add the cost of the trip

    # Calculate the amount Tom will have to pay
    amount_to_pay = total_cost - (medical_cost * 0.8)  # subtract the amount covered by insurance
    result = amount_to_pay
    return result

print(solution())