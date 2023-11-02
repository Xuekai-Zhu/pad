def solution():
    """There are 28 garden gnomes in a yard. Three-fourths of them have red hats, and the rest have blue hats. Half the garden gnomes have big noses instead of small noses. If six gnomes with blue hats have big noses, how many gnomes with red hats have small noses?"""
    # Define the total number of garden gnomes
    total_gnomes = 28

    # Calculate the number of gnomes with red hats and blue hats
    red_hat_gnomes = int(total_gnomes * 3/4)
    blue_hat_gnomes = total_gnomes - red_hat_gnomes

    # Calculate the number of gnomes with big noses and small noses
    big_nose_gnomes = int(total_gnomes / 2)
    small_nose_gnomes = total_gnomes - big_nose_gnomes

    # Calculate the number of gnomes with red hats and small noses
    blue_big_nose_gnomes = 6
    red_small_nose_gnomes = small_nose_gnomes - blue_big_nose_gnomes
    red_hat_small_nose_gnomes = red_small_nose_gnomes - (red_hat_gnomes - blue_big_nose_gnomes)

    # Display the number of gnomes with red hats and small noses
    result = red_hat_small_nose_gnomes
    return result

print(solution())