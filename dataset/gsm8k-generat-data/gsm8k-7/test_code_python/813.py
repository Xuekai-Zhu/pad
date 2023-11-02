def solution():
    normal_doctor_cost = 200
    discount_percentage = 0.7
    num_visits = 2

    # Calculate the cost of one visit to the discount clinic
    discount_cost = normal_doctor_cost * discount_percentage

    # Calculate the total cost of two visits to the discount clinic
    total_cost = discount_cost * num_visits

    # Calculate the amount of money saved compared to visiting a normal doctor twice
    money_saved = (normal_doctor_cost * num_visits) - total_cost
    result = money_saved
    return result

print(solution())