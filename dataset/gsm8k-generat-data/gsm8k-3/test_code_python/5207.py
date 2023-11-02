def solution():
    """Geric had twice as many bills as Kyla who has 2 fewer bills than Jessa.  After giving 3 bills to Geric, Jessa has 7 bills left. How many bills did Geric have at the beginning?"""
    # Let x be the number of bills Kyla has
    # Then Jessa has x+2 bills
    # And Geric has 2x bills
    x = (Jessa's bills count) - 2
    geric_bills = 2 * x
    jessa_bills = x + 2
    jessa_bills -= 3  # Jessa gives 3 bills to Geric
    if jessa_bills == 7:  # Jessa has 7 bills left
        result = geric_bills
    else:
        result = None
    return result

print(solution())