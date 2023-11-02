def solution():
    total_spent = 150

    # Let x represent the amount of money that Pop spent
    # Crackle spent 3x and Snap spent 2(3x)=6x
    x = total_spent / (1 + 3 + 6)

    # Calculate how much Pop spent (3x)
    pop_spent = 3 * x
    result = pop_spent
    return result

print(solution())