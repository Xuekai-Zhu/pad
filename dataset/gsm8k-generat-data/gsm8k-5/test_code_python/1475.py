def solution():
    total_marbles = 10  # Pete has 10 marbles in total

    # Calculate the number of blue marbles
    num_blue_marbles = int(total_marbles * 0.4)  # 40% of the marbles are blue

    # Calculate the number of red marbles
    num_red_marbles = total_marbles - num_blue_marbles

    # Pete keeps 1 red marble, so he will trade the rest
    num_red_to_trade = num_red_marbles - 1
    num_blue_to_trade = num_red_to_trade * 2

    # Calculate the new total number of marbles after trading
    new_total_marbles = total_marbles - num_red_to_trade + num_blue_to_trade
    result = new_total_marbles
    return result

print(solution())