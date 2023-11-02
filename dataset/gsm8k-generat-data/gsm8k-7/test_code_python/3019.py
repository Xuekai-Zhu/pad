def solution():
    num_green_marbles = 26
    num_bags_of_blue_marbles = 6
    blue_marbles_per_bag = 10
    num_green_gift_marbles = 6
    num_blue_gift_marbles = 8

    # Calculate the total number of blue marbles that Janelle bought
    total_blue_marbles = num_bags_of_blue_marbles * blue_marbles_per_bag

    # Calculate the total number of green marbles after buying blue marbles
    total_green_marbles = num_green_marbles

    # Calculate the total number of blue marbles after buying blue marbles
    total_blue_marbles += total_blue_marbles

    # Calculate the total number of marbles in the gift
    total_gift_marbles = num_green_gift_marbles + num_blue_gift_marbles

    # Calculate the final number of marbles
    final_num_marbles = total_green_marbles + total_blue_marbles - total_gift_marbles
    result = final_num_marbles
    return result

print(solution())