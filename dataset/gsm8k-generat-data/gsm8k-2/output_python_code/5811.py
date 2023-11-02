def solution():
    """A store owner repacked his oils into 200 mL bottles. He was able to make 20 bottles. How many liters of oil did the store owner have?"""
    bottle_volume = 200 / 1000 # convert milliliters to liters
    num_bottles = 20
    total_volume = bottle_volume * num_bottles
    result = total_volume
    return result

print(solution())