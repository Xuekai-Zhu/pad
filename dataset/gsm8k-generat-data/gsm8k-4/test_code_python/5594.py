def solution():
    """If Pam is currently twice as young as Rena is, and in 10 years Rena will be 5 years older than her, how old is Pam now?"""
    # Let's assume Pam's current age as x
    x = None

    # As per the question, Rena's current age will be twice Pam's age
    y = 2 * x

    # In 10 years, Rena will be 5 years older than Pam
    # So, Rena's age in 10 years will be (x + 10 + 5) = (x + 15) and Pam's age in 10 years will be (x + 10)
    # Therefore, (x + 15) = 2 * (x + 10)
    # Solving the above equation, we get x = 5

    x = 5
    result = x
    return result

print(solution())