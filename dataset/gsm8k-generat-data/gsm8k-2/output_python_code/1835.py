def solution():
    """Caleb, Andy and Billy went on a picnic with their father. Billy took 6 candies with him, Caleb took 11 and Andy left with 9. On the way, their father bought a packet of 36 candies. He gave 8 candies to Billy, 11 to Caleb and the rest to Andy. How many more candies does Andy now have than Caleb?"""
    billy_candies = 6
    caleb_candies = 11
    andy_candies = 9
    father_candies = 36
    father_candies -= 8  # give 8 to Billy
    billy_candies += 8
    father_candies -= 11  # give 11 to Caleb
    caleb_candies += 11
    andy_candies += father_candies  # give rest to Andy
    difference = andy_candies - caleb_candies
    result = difference
    return result

print(solution())