def solution():
    
    total_flowers = 52
    flowers_given_to_mom = 15
    flowers_given_to_grandma = flowers_given_to_mom + 6
    flowers_in_vase = total_flowers - (flowers_given_to_mom + flowers_given_to_grandma)
    result = flowers_in_vase
    return result

print(solution())