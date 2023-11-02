def solution():
    # Find the number of eggs needed by Ked per week
    eggs_Ked = 0.5 * 14  # Ked needs half of the number of eggs needed by Ben
    
    # Calculate the total number of eggs needed per week in the community
    eggs_per_week = 10 + 14 + eggs_Ked
    
    # Calculate the total number of eggs needed per month
    eggs_per_month = eggs_per_week * 4
    
    result = eggs_per_month
    return result

print(solution())