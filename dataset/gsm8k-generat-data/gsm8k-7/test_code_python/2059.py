def solution():
    num_blue_marbles = 7
    num_red_marbles = 11
    prob_yellow_marble = 1/4

    # Calculate total number of marbles
    total_marbles = num_blue_marbles + num_red_marbles + num_yellow_marbles

    # Calculate the probability of picking a yellow marble
    prob_blue_marble = num_blue_marbles / total_marbles
    prob_red_marble = num_red_marbles / total_marbles
    prob_total = prob_blue_marble + prob_red_marble + prob_yellow_marble

    # Solve for num_yellow_marbles using proportion
    num_yellow_marbles = (prob_yellow_marble/prob_total) * total_marbles
    result = num_yellow_marbles
    return result

print(solution())