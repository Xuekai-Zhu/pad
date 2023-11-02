def solution():
    
    clowns = 4
    children = 30
    total_people = clowns + children
    candies = 700
    sold_candies = total_people * 20
    remaining_candies = candies - sold_candies
    result = remaining_candies
    return result

print(solution())