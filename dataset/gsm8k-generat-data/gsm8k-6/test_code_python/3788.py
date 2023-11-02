def solution():
    # Calculate the number of fish Mabel counts on day 1 and day 2
    day_1_fish = 15
    day_2_fish = 3 * day_1_fish

    # Calculate the number of sharks Mabel counted over the two days
    total_fish = day_1_fish + day_2_fish
    num_sharks = 0.25 * total_fish

    result = num_sharks
    return result

print(solution())