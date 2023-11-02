def solution():
    """Jeremy's uncle gave him $50 to spend on basketball equipment. He bought 5 jerseys that cost $2 each, a basketball that cost $18, and a pair of shorts that cost $8. How much money does Jeremy have left?"""
    
    # Define the initial amount of money given to Jeremy
    initial_amount = 50
    
    # Define the cost of each item
    jersey_cost = 2
    basketball_cost = 18
    shorts_cost = 8
    
    # Define the number of each item purchased
    num_jerseys = 5
    num_basketballs = 1
    num_shorts = 1
    
    # Calculate the total cost of the items purchased
    total_cost = (jersey_cost * num_jerseys) + (basketball_cost * num_basketballs) + (shorts_cost * num_shorts)
    
    # Calculate the amount of money Jeremy has left
    money_left = initial_amount - total_cost
    
    # Display the amount of money Jeremy has left
    result = money_left
    return result

print(solution())