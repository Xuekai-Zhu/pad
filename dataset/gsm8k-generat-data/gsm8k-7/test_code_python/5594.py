def solution():
    # Let's assume Pam's current age is x
    x = 0
    # Rena's current age is twice as old as Pam's
    y = x * 2
    # In ten years, Rena will be 5 years older than Pam
    if y + 10 == x + 10 + 5:
        # Solving the equation, we get Pam's current age
        x = 15
    result = x
    return result

print(solution())