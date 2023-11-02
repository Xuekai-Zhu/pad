def solution():
    # Calculate the number of months it takes for the grass to grow from 2 inches to 4 inches
    growth_per_month = 0.5
    growth_needed = 2
    months_to_grow = (growth_needed / growth_per_month)

    # Calculate the number of times John needs to cut the grass in a year
    months_in_year = 12
    cuts_per_year = months_in_year / months_to_grow

    # Calculate the cost per grass cutting
    cost_per_cutting = 100

    # Calculate the total cost per year
    total_cost = cuts_per_year * cost_per_cutting
    result = total_cost
    return result

print(solution())