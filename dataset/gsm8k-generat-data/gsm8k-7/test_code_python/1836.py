def solution():
    billy_candies = 6
    caleb_candies = 11
    andy_candies = 9
    bought_candies = 36

    # Calculate the total number of candies the father gave to Billy and Caleb
    given_candies = 8 + 11

    # Calculate the number of candies that the father gave to Andy
    andy_given_candies = bought_candies - given_candies

    # Calculate the number of candies that Andy has now
    andy_total_candies = andy_candies + andy_given_candies

    # Calculate the number of candies that Caleb has now
    caleb_total_candies = caleb_candies + 11

    # Calculate the difference in the number of candies that Andy and Caleb have
    difference = andy_total_candies - caleb_total_candies
    result = difference
    return result

print(solution())