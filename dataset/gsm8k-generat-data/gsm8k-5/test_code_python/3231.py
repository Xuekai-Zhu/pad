def solution():
    total_bread = 200  # Lucca bought 200 pieces of bread
    day1_bread = total_bread * (1/4)  # Lucca ate 1/4 of the bread on the first day
    remaining_bread1 = total_bread - day1_bread  # Calculate the remaining bread after day 1
    day2_bread = remaining_bread1 * (2/5)  # Lucca ate 2/5 of the remaining bread on the second day
    remaining_bread2 = remaining_bread1 - day2_bread  # Calculate the remaining bread after day 2
    day3_bread = remaining_bread2 * (1/2)  # Lucca ate half of the remaining bread on the third day
    remaining_bread3 = remaining_bread2 - day3_bread  # Calculate the remaining bread after day 3
    result = remaining_bread3
    return result

print(solution())