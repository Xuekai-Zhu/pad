def solution():
    oysters_price = 15.0  # per dozen
    num_dozen_oysters = 3
    shrimp_price = 14.0  # per pound
    num_pounds_shrimp = 2
    clams_price = 13.5  # per pound
    num_pounds_clams = 2
    num_people = 4

    # Calculate the total cost of oysters
    total_oysters_cost = oysters_price * num_dozen_oysters

    # Calculate the total cost of shrimp
    total_shrimp_cost = shrimp_price * num_pounds_shrimp

    # Calculate the total cost of clams
    total_clams_cost = clams_price * num_pounds_clams

    # Calculate the total cost of the meal
    total_cost = total_oysters_cost + total_shrimp_cost + total_clams_cost

    # Calculate the cost per person
    cost_per_person = total_cost / num_people
    result = cost_per_person
    return result

print(solution())