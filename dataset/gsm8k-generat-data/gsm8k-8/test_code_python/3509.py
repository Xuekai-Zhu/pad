def solution():
    # Define Scott's weekly running distances
    monday_wednesday_distance = 3
    thursday_friday_distance = monday_wednesday_distance * 2

    # Calculate Scott's total monthly running distance
    monthly_distance = (monday_wednesday_distance * 3 + thursday_friday_distance * 2) * 4
    result = monthly_distance
    return result

print(solution())