def solution():
    
    bag1 = 20
    bag2 = 20
    bag3 = 20
    bag4 = 20
    bag5 = 25
    bag6 = 25
    bag7 = 25
    bag8 = 25
    bag9 = 25
    bag10 = 25
    total_apples = bag1 + bag2 + bag3 + bag4 + bag5 + bag6 + bag7 + bag8 + bag9 + bag10
    sold_apples = 200
    remaining_apples = total_apples - sold_apples
    result = remaining_apples
    return result

print(solution())