def solution():
    """If Pam is currently twice as young as Rena is, and in 10 years Rena will be 5 years older than her, how old is Pam now?"""
    # Let's assume Pam is x years old currently
    x = 0

    # Let's set up the equation based on the given information
    # Rena is currently y years old
    # Pam is currently twice as young as Rena, so x = 2y
    # In 10 years, Rena will be 5 years older than Pam, so y+10 = x+15
    # We can substitute x=2y into the second equation to get y+10 = 2y+15
    # Solving for y, we get y = 5, which means x = 2y = 10
    # Therefore, Pam is currently 10 years old
    result = x
    return result

print(solution())