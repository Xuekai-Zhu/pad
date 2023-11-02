def solution():
    apples_on_tree = 5
    apples_on_ground = 8
    apples_eaten_by_dog = 3
    apples_left = apples_on_tree + apples_on_ground - apples_eaten_by_dog
    result = apples_left
    return result

print(solution())