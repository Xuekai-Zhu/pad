def solution():
    # Define the total number of gnomes
    total_gnomes = 28

    # Calculate the number of gnomes with red hats
    red_hat_gnomes = 0.75 * total_gnomes

    # Calculate the number of gnomes with blue hats
    blue_hat_gnomes = total_gnomes - red_hat_gnomes

    # Calculate the total number of gnomes with big noses
    total_big_nose_gnomes = 0.5 * total_gnomes

    # Calculate the number of gnomes with blue hats and big noses
    blue_hat_big_nose_gnomes = 6

    # Calculate the number of gnomes with red hats and small noses
    red_hat_small_nose_gnomes = red_hat_gnomes - (total_big_nose_gnomes - blue_hat_big_nose_gnomes)

    result = red_hat_small_nose_gnomes
    return result

print(solution())