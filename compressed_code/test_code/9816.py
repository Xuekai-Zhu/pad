def solution():
    
    grapes = 100
    strawberries = (3/5) * grapes
    total_fruits = grapes + strawberries
    each_friend_gets = (1/5) * total_fruits
    remaining_fruits = total_fruits - (each_friend_gets * 2)
    result = remaining_fruits
    return result

print(solution())