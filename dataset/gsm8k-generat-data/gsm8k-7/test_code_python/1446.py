def solution():
    num_ties = 34
    num_belts = 40
    num_black_shirts = 63
    num_white_shirts = 42

    # Calculate the total number of black and white shirts
    total_black_white_shirts = num_black_shirts + num_white_shirts

    # Calculate the number of jeans
    num_jeans = (2/3) * total_black_white_shirts

    # Calculate the sum of ties and belts
    sum_ties_belts = num_ties + num_belts

    # Calculate the number of scarves
    num_scarves = 0.5 * sum_ties_belts

    # Calculate the difference between the number of jeans and scarves
    diff_jeans_scarves = num_jeans - num_scarves
    result = diff_jeans_scarves
    return result

print(solution())