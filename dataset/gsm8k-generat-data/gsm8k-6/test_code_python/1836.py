def solution():
    # Calculate the total number of candies each of the children has
    billy_candies = 6 + 8
    caleb_candies = 11 + 11
    andy_candies = 9 + (36-8-11)

    # Calculate the difference in candies between Andy and Caleb
    difference = andy_candies - caleb_candies
    result = difference
    return result

print(solution())