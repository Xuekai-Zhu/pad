def solution():
    """Bobby can deadlift 300 pounds at 13. When he is 18 he can deadlift 100 pounds more than 250% of his previous deadlift. How many pounds did he add per year?"""
    starting_deadlift = 300
    ending_deadlift = 250/100 * starting_deadlift + 100
    years_passed = 18 - 13
    pounds_added_per_year = (ending_deadlift - starting_deadlift) / years_passed
    result = pounds_added_per_year
    return result

print(solution())