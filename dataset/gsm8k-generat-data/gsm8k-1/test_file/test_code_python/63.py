def solution():
    """A treasure hunter found a buried treasure chest filled with gems. There were 175 diamonds, 35 fewer rubies than diamonds, and twice the number of emeralds than the rubies. How many of the gems were there in the chest?"""
    diamonds = 175
    rubies = diamonds - 35
    emeralds = rubies * 2
    total_gems = diamonds + rubies + emeralds
    result = total_gems
    return result

print(solution())