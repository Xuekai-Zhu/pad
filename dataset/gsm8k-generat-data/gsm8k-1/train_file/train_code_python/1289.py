def solution():
    """Andy is mixing blue, green and white paint in a 1 : 2 : 5 ratio. If he uses 6 gallons of green paint, how many gallons of paint does he use total?"""
    green_ratio = 2 # ratio of green paint in the mixture
    total_ratio = 1 + green_ratio + 5 # total ratio of all paint colors in the mixture
    green_paint = 6 # amount of green paint used
    total_paint = green_paint * (total_ratio / green_ratio) # calculation based on ratios
    
    result = total_paint
    return result

print(solution())