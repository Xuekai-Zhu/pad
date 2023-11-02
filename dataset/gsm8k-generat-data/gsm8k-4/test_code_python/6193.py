def solution():
    """Clinton has twice as many shoes in his wardrobe as belts. He has 2 more belts than hats and currently has 5 hats. How many shoes does Clinton have?"""
    # Number of hats
    hats = 5
    
    # Number of belts
    belts = hats + 2
    
    # Number of shoes is twice the number of belts
    shoes = 2 * belts
    
    result = shoes
    return result

print(solution())