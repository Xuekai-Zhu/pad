def solution():
    # Calculate the number of fish Mabel saw on day one
    day1_fish = 15

    # Calculate the number of fish Mabel saw on day two
    day2_fish = 3 * day1_fish

    # Calculate the total number of fish Mabel saw
    total_fish = day1_fish + day2_fish

    # Calculate the number of sharks Mabel saw
    sharks = total_fish * 0.25
    result = sharks
    return result

print(solution())