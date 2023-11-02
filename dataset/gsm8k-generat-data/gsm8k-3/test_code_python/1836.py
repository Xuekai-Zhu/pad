def solution():
    """Caleb, Andy and Billy went on a picnic with their father. Billy took 6 candies with him, Caleb took 11 and Andy left with 9. On the way, their father bought a packet of 36 candies. He gave 8 candies to Billy, 11 to Caleb and the rest to Andy. How many more candies does Andy now have than Caleb?"""
    # Define the initial number of candies each person has
    billy_candies = 6
    caleb_candies = 11
    andy_candies = 9

    # Define the number of candies their father bought and distributed
    father_candies = 36
    billy_extra_candies = 8
    caleb_extra_candies = 11
    andy_extra_candies = father_candies - billy_extra_candies - caleb_extra_candies

    # Calculate the final number of candies each person has
    billy_candies += billy_extra_candies
    caleb_candies += caleb_extra_candies
    andy_candies += andy_extra_candies

    # Calculate the difference between Andy and Caleb's number of candies
    difference = andy_candies - caleb_candies

    # Display the difference
    result = difference
    return result

print(solution())