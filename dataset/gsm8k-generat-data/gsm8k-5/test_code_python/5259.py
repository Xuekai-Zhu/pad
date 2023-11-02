def solution():
    current_fish_in_tank = 20  # The tank currently has 20 fish
    before_addition = current_fish_in_tank - 4  # I had 4 fewer fish before the addition
    added_fish = current_fish_in_tank - before_addition  # The number of fish I added is the difference between current and previous fish count
    result = added_fish
    return result

print(solution())