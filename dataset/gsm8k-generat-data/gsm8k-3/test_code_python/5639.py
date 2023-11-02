def solution():
    """There are 30 major league baseball stadiums. Zach has a goal to take his son to see at least one game at each one. He has calculated the average cost for them to travel and see a game will be $900 per stadium. Zach can save $1,500 per year for his baseball stadium trips. How many years will it take Zach to accomplish his goal?"""
    
    # Define the total cost to visit all the stadiums
    total_cost = 900 * 30
    
    # Define Zach's annual savings 
    annual_savings = 1500
    
    # Calculate the number of years it will take Zach to save enough money
    years_to_save = total_cost / annual_savings
    
    # Display the number of years it will take Zach
    result = years_to_save
    return result

print(solution())