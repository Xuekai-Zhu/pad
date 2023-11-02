def solution():
    """Candice buys all the bread she and her family needs for the week from a local bakery. 
    She needs 2 loaves of white bread for sandwiches that cost $3.50 each. 
    She also needs a baguette that costs $1.50 and 2 loaves of sourdough bread that cost $4.50 each. 
    She also treats herself to a $2.00 almond croissant each visit. 
    How much does Candice spend at the bakery over 4 weeks?"""
    
    # Define the cost of each item
    WHITE_BREAD_COST = 3.50
    BAGUETTE_COST = 1.50
    SOURDOUGH_BREAD_COST = 4.50
    CROISSANT_COST = 2.00
    
    # Define the number of each item needed per week
    white_bread_per_week = 2
    baguette_per_week = 1
    sourdough_bread_per_week = 2
    croissant_per_week = 1
    
    # Calculate the total cost per week
    total_cost_per_week = (white_bread_per_week * WHITE_BREAD_COST) + (baguette_per_week * BAGUETTE_COST) + (sourdough_bread_per_week * SOURDOUGH_BREAD_COST) + (croissant_per_week * CROISSANT_COST)
    
    # Calculate the total cost over 4 weeks
    total_cost = total_cost_per_week * 4
    
    # Display the total cost
    result = total_cost
    return result

print(solution())