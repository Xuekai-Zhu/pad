def solution():
    # Calculate the total number of candies in the box
    yellow_candies = 10 + 4  # 4 more yellow candies than purple candies
    green_candies = yellow_candies - 2  # 2 fewer green candies than yellow candies
    total_candies = purple_candies + yellow_candies + green_candies
    result = total_candies
    return result

print(solution())