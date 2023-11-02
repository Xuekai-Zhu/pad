def solution():
    
    starting_deadlift = 300
    ending_deadlift = 250/100 * starting_deadlift + 100
    years_passed = 18 - 13
    pounds_added_per_year = (ending_deadlift - starting_deadlift) / years_passed
    result = pounds_added_per_year
    return result

print(solution())