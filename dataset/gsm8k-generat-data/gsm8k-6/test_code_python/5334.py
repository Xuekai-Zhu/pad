def solution():
    # Calculate the total number of pencils Judy needs for 45 days of school
    total_pencils = 10 * 9  # Judy goes to school for 9 weeks (45 days)
    
    # Calculate the total cost of the pencils
    cost_per_pencil = 4/30  # cost per pencil in the 30 pack
    total_cost = cost_per_pencil * total_pencils
    
    result = total_cost
    return result

print(solution())