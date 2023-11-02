def solution():
    """Karen wanted to go out to get some fast food. She pulls up to the drive-through and orders a 5-dollar burger. Her son then yelled out that he wanted a 4-dollar sandwich, so it was added to the order. Karen then decided to order some drinks and opted for two 4-dollar smoothies. What is the total cost of Karen's fast-food order?"""
    # Define the cost of the burger, sandwich, and smoothies
    burger_cost = 5
    sandwich_cost = 4
    smoothie_cost = 4
    
    # Calculate the total cost of the order
    total_cost = burger_cost + sandwich_cost + (2 * smoothie_cost)
    
    # Return the result
    result = total_cost
    return result

print(solution())