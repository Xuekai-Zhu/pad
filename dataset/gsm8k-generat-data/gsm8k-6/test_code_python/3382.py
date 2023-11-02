def solution():
    # Calculate the number of vacation days Andrew has earned from his 300 days worked
    earned_vacation_days = 300 // 10  # for every 10 days worked, you get 1 vacation day
    
    # Subtract the number of vacation days Andrew has already taken
    taken_vacation_days = 5 + (2 * 5)  # Andrew took 5 days off in March and twice as many (10) in September
    remaining_vacation_days = earned_vacation_days - taken_vacation_days
    
    result = remaining_vacation_days
    return result

print(solution())