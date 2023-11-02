def solution():
    rob_grapes = 25
    allie_grapes = rob_grapes + 2
    allyn_grapes = allie_grapes + 4

    # Calculate the total number of grapes in all three bowls
    total_grapes = rob_grapes + allie_grapes + allyn_grapes
    result = total_grapes
    return result

print(solution())