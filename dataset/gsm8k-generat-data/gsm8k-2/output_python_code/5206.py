def solution():
    """Geric had twice as many bills as Kyla who has 2 fewer bills than Jessa.
    After giving 3 bills to Geric, Jessa has 7 bills left. How many bills did Geric have at the beginning?"""
    jessa_bills = 10
    kyla_bills = jessa_bills - 2
    geric_bills = 2 * kyla_bills
    jessa_bills -= 3
    geric_bills += 3
    total_bills = geric_bills + jessa_bills + kyla_bills

    result = geric_bills
    return result

print(solution())