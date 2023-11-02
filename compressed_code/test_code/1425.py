def solution():
    
    billy_candies = 6
    caleb_candies = 11
    andy_candies = 9
    father_candies = 36
    father_candies -= 8  
    billy_candies += 8
    father_candies -= 11  
    caleb_candies += 11
    andy_candies += father_candies  
    difference = andy_candies - caleb_candies
    result = difference
    return result

print(solution())