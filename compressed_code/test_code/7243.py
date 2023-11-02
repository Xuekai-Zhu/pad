def solution():
    
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