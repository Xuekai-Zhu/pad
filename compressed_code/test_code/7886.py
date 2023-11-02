def solution():
    
    total_apples = 55
    apples_given_away = 10
    apples_remaining = total_apples - apples_given_away
    friends = 4
    apples_per_person = apples_remaining / (friends + 1) 
    result = apples_per_person
    return result

print(solution())