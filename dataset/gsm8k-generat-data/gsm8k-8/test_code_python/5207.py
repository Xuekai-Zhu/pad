def solution():
    # Define the number of bills Kyla has
    kyla_bills = 7 + 2

    # Define the number of bills Geric has
    geric_bills = 2 * kyla_bills

    # Jessa gives 3 bills to Geric, so she has 7 + 2 - 3 = 6 bills left
    jessa_bills = 6

    # Check the solution by verifying that Geric had twice as many bills as Kyla and that Jessa has 2 fewer bills than Kyla
    assert geric_bills == 2 * kyla_bills
    assert jessa_bills == kyla_bills - 2

    result = geric_bills
    return result

print(solution())