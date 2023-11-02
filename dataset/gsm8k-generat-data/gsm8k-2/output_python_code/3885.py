def solution():
    """Rebecca bought 22 items for her camping trip, including tent stakes, packets of drink mix, and bottles of water. She bought 3 times as many packets of drink mix as tent stakes. She also bought 2 more bottles of water than she did tent stakes. How many tent stakes did she buy?"""
    total_items = 22
    drink_mix = 3
    bottles_of_water = 2
    tent_stakes = (total_items / (1 + drink_mix + bottles_of_water)) 
    result = tent_stakes
    return result

print(solution())