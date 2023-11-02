def solution():
    """A bottle can hold 2 cups of water. How many cups of water are needed to fill up 10 whole bottles and 5 half-capacity bottles?"""
    full_bottles = 10
    half_bottles = 5
    cups_per_bottle = 2
    total_cups = (full_bottles * cups_per_bottle) + (half_bottles * cups_per_bottle * 0.5)
    result = total_cups
    return result

print(solution())