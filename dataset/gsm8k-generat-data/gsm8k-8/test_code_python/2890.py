def solution():
    # Define Dave's initial amount
    dave_amount = 46

    # Calculate Kyle's initial amount
    kyle_amount = 3*dave_amount - 12

    # Calculate how much Kyle spends snowboarding
    snowboarding_spending = kyle_amount / 3

    # Calculate Kyle's final amount
    kyle_amount -= snowboarding_spending

    result = kyle_amount
    return result

print(solution())