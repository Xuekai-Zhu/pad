def solution():
    """Caleb, Andy and Billy went on a picnic with their father. Billy took 6 candies with him, Caleb took 11 and Andy left with 9. On the way, their father bought a packet of 36 candies. He gave 8 candies to Billy, 11 to Caleb and the rest to Andy. How many more candies does Andy now have than Caleb?"""
    billy_candies = 6
    caleb_candies = 11
    andy_candies = 9
    candies_bought = 36
    candies_to_billy = 8
    candies_to_caleb = 11
    candies_to_andy = candies_bought - candies_to_billy - candies_to_caleb
    andy_total_candies = andy_candies + candies_to_andy
    caleb_total_candies = caleb_candies + candies_to_caleb
    more_candies = andy_total_candies - caleb_total_candies
    result = more_candies
    return result

print(solution())