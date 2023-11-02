def solution():
    price_per_person = 147
    discount = 14
    num_people = 2

    # Calculate the total cost without discount
    cost_without_discount = price_per_person * num_people

    # Calculate the total discount
    total_discount = discount * num_people

    # Calculate the total cost with discount
    total_cost = cost_without_discount - total_discount
    result = total_cost
    return result

print(solution())