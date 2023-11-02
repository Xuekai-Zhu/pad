def solution():
    """There are 60 pieces of chips in Lara's bag. One-sixth of the chips are blue. There are 34 red chips and the rest are green. How many green chips are in Lara's bag?"""
    total_chips = 60
    blue_chips = total_chips / 6
    red_chips = 34
    green_chips = total_chips - blue_chips - red_chips
    result = green_chips
    return result

print(solution())