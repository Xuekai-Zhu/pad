def solution():
    total_chips = 60  # There are 60 pieces of chips in Lara's bag
    blue_chips = total_chips / 6  # One-sixth of the chips are blue
    red_chips = 34  # There are 34 red chips
    green_chips = total_chips - blue_chips - red_chips  # The remaining chips are green
    result = green_chips
    return result

print(solution())