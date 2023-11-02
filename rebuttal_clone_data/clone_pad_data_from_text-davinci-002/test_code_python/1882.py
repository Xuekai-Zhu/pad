def solution():
    bananas_on_tree = 100
    bananas_eaten = 70
    bananas_remaining = 2 * (bananas_on_tree - bananas_eaten)
    result = bananas_on_tree + bananas_remaining
    return result

print(solution())