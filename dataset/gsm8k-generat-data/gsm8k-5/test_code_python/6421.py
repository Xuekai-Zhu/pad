def solution():
    rob_grapes = 25  # Rob's bowl contained 25 grapes
    allie_grapes = rob_grapes + 2  # Allie's bowl contained two more grapes than Rob's bowl
    allyn_grapes = allie_grapes + 4  # Allyn's bowl contained four more grapes than Allie's bowl

    # Calculate the total number of grapes in all three bowls
    total_grapes = rob_grapes + allie_grapes + allyn_grapes
    result = total_grapes
    return result

print(solution())