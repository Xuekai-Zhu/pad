def solution():
    """Jane's mother agreed to pay her $.50 for every flower bulb that Jane planted. Jane planted 20 tulip bulbs and half that amount of iris bulbs. She also planted 30 daffodil bulbs and three times that amount of crocus bulbs. How much money did Jane earn?"""
    
    # Calculate the number of iris bulbs planted
    iris_bulbs = 20 / 2
    
    # Calculate the number of crocus bulbs planted
    crocus_bulbs = 30 * 3
    
    # Calculate the total number of flower bulbs planted
    total_bulbs = 20 + iris_bulbs + 30 + crocus_bulbs
    
    # Calculate Jane's earnings
    earnings = total_bulbs * 0.5
    
    result = earnings
    return result

print(solution())