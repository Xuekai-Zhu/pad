def solution():
    total_earnings = 30
    cost_per_person = 2.5
    num_people = 10

    # Calculate the total cost of the pool trip
    total_cost = cost_per_person * num_people

    # Calculate the amount left after the pool trip
    amount_left = total_earnings - total_cost
    result = amount_left
    return result

print(solution())