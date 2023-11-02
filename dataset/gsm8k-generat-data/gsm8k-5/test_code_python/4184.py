def solution():
    total_gnomes = 28  # There are 28 garden gnomes in total
    red_hat_gnomes = (3/4) * total_gnomes  # Three-fourths of the gnomes have red hats
    blue_hat_gnomes = total_gnomes - red_hat_gnomes  # The rest of the gnomes have blue hats
    big_nose_gnomes = total_gnomes / 2  # Half the gnomes have big noses
    small_nose_gnomes = total_gnomes - big_nose_gnomes  # The rest have small noses

    # Calculate the number of gnomes with red hats and big noses
    red_big_nose_gnomes = 6  # 6 gnomes with blue hats have big noses, we don't have information for red hat gnomes
    # Therefore, we cannot calculate the number of red hat gnomes with big noses

    # Calculate the number of gnomes with red hats and small noses
    red_small_nose_gnomes = red_hat_gnomes - red_big_nose_gnomes  # This is the remaining number of red hat gnomes
    result = red_small_nose_gnomes
    return result

print(solution())