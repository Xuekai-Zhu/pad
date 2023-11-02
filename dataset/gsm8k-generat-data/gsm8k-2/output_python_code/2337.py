def solution():
    """A bottle can hold 2 cups of water. How many cups of water are needed to fill up 10 whole bottles and 5 half-capacity bottles?"""
    whole_bottles = 10
    half_bottles = 5
    total_bottles = whole_bottles + half_bottles
    full_capacity_water = whole_bottles * 2
    half_capacity_water = half_bottles * 1
    total_water = full_capacity_water + half_capacity_water
    result = total_water
    return result

print(solution())