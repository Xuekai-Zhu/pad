def solution():
    num_shoes = 6
    num_jerseys = 4
    total_cost = 560

    # Calculate the cost of one jersey as a fraction of one shoe
    jersey_fraction = 1 / 4

    # Calculate the total cost of all jerseys
    jersey_cost = num_jerseys * (jersey_fraction * shoe_cost)

    # Calculate the total cost of all shoes
    total_shoe_cost = (total_cost - jersey_cost) / num_shoes
    result = total_shoe_cost * num_shoes
    return result

print(solution())