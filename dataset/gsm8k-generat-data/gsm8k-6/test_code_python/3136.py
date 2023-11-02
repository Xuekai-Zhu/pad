def solution():
    # Find how many $12 bags Mark can buy
    num_xl_bags = 2 # Mark can buy two $12 bags with his $24

    # Find how much money Mark has left after buying the $12 bags
    remaining_money = 24 - (num_xl_bags * 12)

    # Find the maximum number of $6 bags Mark can buy with the remaining money
    num_med_bags = remaining_money // 6

    # Find the maximum number of $4 bags Mark can buy with the remaining money
    num_small_bags = (remaining_money % 6) // 4

    # Calculate the total number of balloons Mark can buy
    total_balloons = (num_xl_bags * 200) + (num_med_bags * 75) + (num_small_bags * 50)

    result = total_balloons
    return result

print(solution())