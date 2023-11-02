def solution():
    # Define the initial number of candies each child had
    billy_candies = 6
    caleb_candies = 11
    andy_candies = 9

    # Calculate the total number of candies after the father's purchase
    total_candies = billy_candies + caleb_candies + andy_candies + 36

    # Distribute the candies given by the father
    billy_candies += 8
    caleb_candies += 11
    andy_candies += total_candies - (billy_candies + caleb_candies + andy_candies)

    # Calculate the difference in candies between Andy and Caleb
    difference = andy_candies - caleb_candies
    result = difference
    return result

print(solution())