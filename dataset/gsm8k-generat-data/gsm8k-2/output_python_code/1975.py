def solution():
    """Madison makes 30 paper boats and sets them afloat. 20% are eaten by fish and Madison shoots two of the others with flaming arrows. How many boats are left?"""
    total_boats = 30
    fish_eaten = 0.2 * total_boats
    remaining_boats = total_boats - fish_eaten - 2
    result = remaining_boats
    return result

print(solution())