def solution():
    """ Caleb, Andy and Billy went on a picnic with their father. Billy took 6 candies with him, Caleb took 11 and Andy left with 9. On the way, their father bought a packet of 36 candies. He gave 8 candies to Billy, 11 to Caleb and the rest to Andy. How many more candies does Andy now have than Caleb? """
    # Define the initial number of candies each person has
    billy_candies = 6
    caleb_candies = 11
    andy_candies = 9

    # Define the number of candies their father bought
    father_candies = 36

    # Calculate how many candies each person gets from their father
    billy_candies += 8
    caleb_candies += 11
    andy_candies += father_candies - 8 - 11

    # Calculate the difference in candies between Andy and Caleb
    difference = andy_candies - caleb_candies

    # Return the result
    result = difference
    return result

print(solution())