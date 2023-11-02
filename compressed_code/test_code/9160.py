def solution():
    
    total_candies = 60
    candies_given = 20
    packs_remaining = (total_candies - candies_given) // 20
    result = packs_remaining
    return result

print(solution())