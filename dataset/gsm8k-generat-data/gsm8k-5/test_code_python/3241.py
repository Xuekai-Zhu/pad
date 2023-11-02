def solution():
    fish_per_roll = 40  # James needs 40 fish to make a sushi roll
    total_fish = 400  # James bought 400 fish
    bad_fish = total_fish * 0.2  # 20% of the fish are bad
    remaining_fish = total_fish - bad_fish  # James can only use the remaining fish
    rolls = remaining_fish // fish_per_roll  # Calculate how many sushi rolls James can make

    result = rolls
    return result

print(solution())