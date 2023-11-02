def solution():
    
    people_abducted = 200
    people_returned = people_abducted * 0.8
    people_left = people_abducted - people_returned
    people_home = people_left - 10
    result = people_home
    return result

print(solution())