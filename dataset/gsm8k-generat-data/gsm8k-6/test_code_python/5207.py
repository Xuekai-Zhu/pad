def solution():
    # Let's assume Kyla has x bills, then Jessa has x+2 bills
    kyla_bills = x
    jessa_bills = x+2

    # Geric has twice as many bills as Kyla
    geric_bills = 2 * kyla_bills

    # After giving 3 bills to Geric, Jessa has 7 bills left
    jessa_bills -= 3
    geric_bills += 3

    # Using the given information, solve for Kyla's number of bills
    kyla_bills = (jessa_bills + 2)/2

    # Geric had twice as many bills as Kyla at the beginning
    geric_bills = 2 * kyla_bills

    result = geric_bills
    return result

print(solution())