def solution():
    
    rolls = 300
    croissants = 120
    baguettes = 60
    roll_length = 4
    croissant_length = 6
    baguette_length = 2
    total_length = (rolls * roll_length) + (croissants * croissant_length) + (baguettes * baguette_length)
    total_feet = total_length / 12
    result = total_feet
    return result

print(solution())