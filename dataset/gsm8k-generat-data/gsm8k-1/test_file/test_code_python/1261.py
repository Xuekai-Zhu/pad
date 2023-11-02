def solution():
    """Tim wanted to make lemonade for a pool party. For a gallon of lemonade, his recipe called for 1 cup of fresh lemon juice. He found that 6 lemons would yield 1 cup of juice. He figured he would need to make 4 gallons of lemonade for the party. His best friend Allen asked if Tim could make an extra gallon for him that was twice as tart as the other gallons. How many lemons will Tim need?"""
    lemons_per_cup = 6
    cups_per_gallon = 16
    total_gallons = 5
    extra_gallons = 1
    extra_tartness = 2
    lemons_needed = (cups_per_gallon * total_gallons) + (cups_per_gallon * extra_gallons * extra_tartness)
    lemons_needed *= lemons_per_cup
    result = lemons_needed
    return result

print(solution())