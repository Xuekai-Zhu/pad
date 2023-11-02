def solution():
    # Find the number of grapes in Allie's bowl
    allie_grapes = 25 + 2

    # Find the number of grapes in Allyn's bowl
    allyn_grapes = allie_grapes + 4

    # Find the total number of grapes in all three bowls
    total_grapes = 25 + allie_grapes + allyn_grapes

    result = total_grapes
    return result

print(solution())