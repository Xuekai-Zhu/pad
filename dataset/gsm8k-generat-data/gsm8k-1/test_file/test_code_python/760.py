def solution():
    """Leila buys 3 cucumbers from the market. Cucumbers are $2 each. Jack buys 5 tomatoes from the grocery store. Tomatoes are $1 each. Chase buys 1 head of lettuce from the farmer’s market. Lettuce cost $3 each. Together, how much did the three of them spend to make a salad for the potluck?"""
    cucumber_cost = 2
    num_cucumbers = 3
    tomato_cost = 1
    num_tomatoes = 5
    lettuce_cost = 3 
    num_lettuce = 1
    
    total_cost = (cucumber_cost * num_cucumbers) + (tomato_cost * num_tomatoes) + (lettuce_cost * num_lettuce)
    result = total_cost
    return result

print(solution())