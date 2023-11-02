def solution():
    """There are 30 major league baseball stadiums. Zach has a goal to take his son to see at least one game at each one. He has calculated the average cost for them to travel and see a game will be $900 per stadium. Zach can save $1,500 per year for his baseball stadium trips. How many years will it take Zach to accomplish his goal?"""
    num_stadiums = 30
    total_cost = num_stadiums * 900
    savings_per_year = 1500
    years_to_save = total_cost / savings_per_year
    result = years_to_save
    return result

print(solution())