def solution():
    # Calculate the number of men and women in the company before new hires
    men = (2/3) * 90  
    women = 90 - men  

    # Calculate the number of women in the company after new hires
    new_women = women + 10  

    # Calculate the total number of employees in the company after new hires
    total_employees = 90 + 10  

    # Calculate the percentage of women in the company after new hires
    women_percentage = (new_women / total_employees) * 100  
    result = women_percentage
    return result

print(solution())