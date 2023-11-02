def solution():
    
    total_shoes = 200
    monday_shoes = 5
    wednesday_shoes = 15
    friday_shoes = 30
    saturday_shoes = 180
    sunday_shoes = total_shoes - (monday_shoes + wednesday_shoes + friday_shoes) - saturday_shoes
    result = sunday_shoes
    return result

print(solution())