def solution():
    """There are 30 major league baseball stadiums. Zach has a goal to take his son to see at least one game at each one. He has calculated the average cost for them to travel and see a game will be $900 per stadium. Zach can save $1,500 per year for his baseball stadium trips. How many years will it take Zach to accomplish his goal?"""
    # Define the number of stadiums and the average cost per stadium
    NUM_STADIUMS = 30
    COST_PER_STADIUM = 900

    # Define the amount Zach can save per year
    SAVINGS_PER_YEAR = 1500

    # Calculate the total cost of the stadium trips
    total_cost = NUM_STADIUMS * COST_PER_STADIUM

    # Calculate the number of years it will take Zach to save up for the trips
    years = total_cost // SAVINGS_PER_YEAR

    result = years
    return result

print(solution())