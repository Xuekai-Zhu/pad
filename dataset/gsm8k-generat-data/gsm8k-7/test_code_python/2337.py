def solution():
    num_kg = 101
    kg_price = 5.8

    num_1st = 113
    first_price = 5.0

    num_2nd = 107
    second_price = 5.6

    num_3rd = 108
    third_price = 5.25

    # Calculate the total cost of all kindergartener shirts
    kg_cost = num_kg * kg_price

    # Calculate the total cost of all first grader shirts
    first_cost = num_1st * first_price

    # Calculate the total cost of all second grader shirts
    second_cost = num_2nd * second_price

    # Calculate the total cost of all third grader shirts
    third_cost = num_3rd * third_price

    # Calculate the total cost of all shirts
    total_cost = kg_cost + first_cost + second_cost + third_cost
    result = total_cost
    return result

print(solution())