def solution():
    # Calculate the total number of sacks of strawberries needed for all bakeries in one week
    total_sacks_per_week = 2 + 4 + 12  

    # Calculate the total number of sacks of strawberries needed for all bakeries in four weeks
    total_sacks_four_weeks = total_sacks_per_week * 4  
    result = total_sacks_four_weeks
    return result

print(solution())