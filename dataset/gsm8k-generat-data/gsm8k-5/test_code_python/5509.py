def solution():
    purple_candies = 10  # The box contains 10 purple candies
    yellow_candies = purple_candies + 4  # There are 4 more yellow candies than purple candies
    green_candies = yellow_candies - 2  # There are 2 fewer green candies than yellow candies

    # Calculate the total number of candies in the box
    total_candies = purple_candies + yellow_candies + green_candies
    result = total_candies
    return result

print(solution())