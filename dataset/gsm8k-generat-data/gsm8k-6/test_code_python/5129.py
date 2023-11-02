def solution():
    grapes = 100
    strawberries = (3/5) * grapes
    total_fruits_before = grapes + strawberries
    each_friend_gets = (1/5) * total_fruits_before
    total_fruits_left = total_fruits_before - (2 * each_friend_gets)
    result = total_fruits_left
    return result

print(solution())