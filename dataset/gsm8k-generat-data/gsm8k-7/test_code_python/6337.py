def solution():
    num_gold_balloon = 141
    num_silver_balloon = 2 * num_gold_balloon
    num_black_balloon = 150

    # Calculate the total number of balloons
    total_balloons = num_gold_balloon + num_silver_balloon + num_black_balloon
    result = total_balloons
    return result

print(solution())