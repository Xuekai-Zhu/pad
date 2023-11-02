def solution():
    
    
    graham_crackers = 14
    oreos = 15
    cheesecakes_possible = min(graham_crackers//2, oreos//3)
    graham_crackers_left = graham_crackers - cheesecakes_possible*2
    result = graham_crackers_left
    return result

print(solution())