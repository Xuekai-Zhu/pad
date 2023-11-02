def solution():
    """Geric had twice as many bills as Kyla who has 2 fewer bills than Jessa. After giving 3 bills to Geric, Jessa has 7 bills left. How many bills did Geric have at the beginning?"""
    jessa_bills = 10  # assume Jessa had 10 bills to start with
    kyla_bills = jessa_bills - 2
    geric_bills = kyla_bills * 2
    geric_bills += 3  # Geric got 3 bills from Jessa
    result = geric_bills
    return result

print(solution())