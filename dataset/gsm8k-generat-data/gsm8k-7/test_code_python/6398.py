def solution():
    num_years = 2021 - 1989 + 1  # +1 is added to include 2021
    cost_per_plant = 20.0

    # Calculate the total cost of all hydrangea plants purchased by Lily
    total_cost = num_years * cost_per_plant
    result = total_cost
    return result

print(solution())