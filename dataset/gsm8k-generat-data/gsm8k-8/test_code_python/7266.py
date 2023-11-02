def solution():
    # Define the number of candies in the banana jar
    banana_candies = 43

    # Calculate the number of candies in the grape jar
    grape_candies = banana_candies + 5

    # Calculate the number of candies in the peanut butter jar
    peanut_butter_candies = 4 * grape_candies

    result = peanut_butter_candies
    return result

print(solution())