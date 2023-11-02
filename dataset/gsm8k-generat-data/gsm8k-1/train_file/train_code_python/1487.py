def solution():
    """Bella, Monica, and Rachel are friends who like jewelry. Bella has 10 earrings, which is 25% of Monica's earrings, and Monica has twice as many earrings as Rachel. How many earrings do all of the friends have?"""
    bella_earrings = 10
    monica_earrings = bella_earrings / 0.25
    rachel_earrings = monica_earrings / 2
    total_earrings = bella_earrings + monica_earrings + rachel_earrings
    result = total_earrings
    return result

print(solution())