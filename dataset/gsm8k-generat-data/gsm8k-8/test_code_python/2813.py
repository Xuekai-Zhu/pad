def solution():
    # Let the amount spent at the supermarket be x
    # Then the amount spent on fixing the automobile is 3x + 50
    x = (350 - 50) / 3

    # The total amount spent is x + 3x + 50
    total_spent = x + 3*x + 50
    result = total_spent
    return result

print(solution())