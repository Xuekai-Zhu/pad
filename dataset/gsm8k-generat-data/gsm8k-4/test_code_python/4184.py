def solution():
    """There are 28 garden gnomes in a yard. Three-fourths of them have red hats, and the rest have blue hats. Half the garden gnomes have big noses instead of small noses. If six gnomes with blue hats have big noses, how many gnomes with red hats have small noses?"""
    # Define the total number of gnomes and the fraction of gnomes with red hats
    total_gnomes = 28
    red_fraction = 3 / 4

    # Calculate the number of gnomes with red and blue hats
    red_gnomes = int(total_gnomes * red_fraction)
    blue_gnomes = total_gnomes - red_gnomes

    # Calculate the number of gnomes with big noses
    big_nose_gnomes = total_gnomes / 2

    # Calculate the number of gnomes with small noses
    small_nose_gnomes = total_gnomes / 2

    # Calculate the number of gnomes with blue hats and big noses
    blue_big_nose_gnomes = 6

    # Calculate the number of gnomes with red hats and small noses
    red_small_nose_gnomes = small_nose_gnomes - blue_big_nose_gnomes

    # Display the result
    result = red_small_nose_gnomes
    return result

print(solution())