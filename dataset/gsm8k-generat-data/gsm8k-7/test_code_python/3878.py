def solution():
    num_members = 20
    candy_bar_cost = 0.5
    num_candy_bars_per_member = 8

    # Calculate the total number of candy bars sold by the group
    total_candy_bars_sold = num_members * num_candy_bars_per_member

    # Calculate the total earnings from candy bar sales
    total_earnings = total_candy_bars_sold * candy_bar_cost
    result = total_earnings
    return result

print(solution())