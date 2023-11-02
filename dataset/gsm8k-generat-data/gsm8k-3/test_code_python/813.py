def solution():
    """Tom cannot afford a normal doctor, so he goes to a discount clinic that is 70% cheaper.   It takes two visits, though, instead of 1.   A normal doctor charges $200 for a visit.   How much money does he save?"""
    # Define the cost of a visit to a normal doctor
    NORMAL_DOCTOR_COST = 200

    # Define the discount percentage for the discount clinic
    DISCOUNT_PERCENTAGE = 0.7

    # Calculate the cost of a visit to the discount clinic
    discount_clinic_cost = NORMAL_DOCTOR_COST * DISCOUNT_PERCENTAGE

    # Calculate the total cost for two visits to the discount clinic
    total_cost = discount_clinic_cost * 2

    # Calculate the amount of money Tom saved
    savings = NORMAL_DOCTOR_COST * 2 - total_cost

    # Display the savings
    result = savings
    return result

print(solution())