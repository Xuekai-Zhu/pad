def solution():
    """Travis goes through 2 boxes of cereal a week.  If each box costs $3.00 and he eats 2 boxes every week for an entire year, 52 weeks, how much does he spend on cereal?"""
    
    # Define the number of boxes of cereal Travis goes through each week
    boxes_per_week = 2
    
    # Define the cost of each box of cereal
    cost_per_box = 3.00
    
    # Calculate the total cost of cereal for the year
    total_cost = boxes_per_week * cost_per_box * 52
    
    # Display the total cost
    result = total_cost
    return result

print(solution())