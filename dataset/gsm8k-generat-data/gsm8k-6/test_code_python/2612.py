def solution():
    # Calculate the number of pounds of cat litter needed for 210 days
    total_litter_needed = 15 * 7 * 30  # 15 pounds per week, 7 days per week, 30 weeks in 210 days

    # Calculate the number of 45-pound containers needed
    num_containers = total_litter_needed / 45 

    # Calculate the total cost
    total_cost = num_containers * 21

    result = total_cost
    return result

print(solution())