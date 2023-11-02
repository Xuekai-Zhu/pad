def solution():
    # Define the number of yellow flowers
    yellow_flowers = 10

    # Calculate the number of purple flowers
    purple_flowers = yellow_flowers * 1.8

    # Calculate the total number of yellow and purple flowers
    yellow_and_purple_flowers = yellow_flowers + purple_flowers

    # Calculate the number of green flowers
    green_flowers = yellow_and_purple_flowers * 0.25

    # Calculate the total number of flowers
    total_flowers = yellow_flowers + purple_flowers + green_flowers
    result = total_flowers
    return result

print(solution())