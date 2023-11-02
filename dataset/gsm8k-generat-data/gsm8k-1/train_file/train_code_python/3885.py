def solution():
    """Rebecca bought 22 items for her camping trip, including tent stakes, packets of drink mix, and bottles of water. She bought 3 times as many packets of drink mix as tent stakes. She also bought 2 more bottles of water than she did tent stakes. How many tent stakes did she buy?"""
    total_items = 22
    packets_per_tent_stake = 3
    water_per_tent_stake = 2
    tent_stakes = (total_items - (packets_per_tent_stake + water_per_tent_stake)) / 2
    result = tent_stakes
    return result

print(solution())