def solution():
    bess = 2  # Bess gives 2 pails of milk every day
    brownie = 3 * bess  # Brownie produces three times the amount Bess does
    daisy = bess + 1  # Daisy makes one more pail than Bess

    # Calculate the total amount of milk from all three cows every week
    weekly_milk = 7 * (bess + brownie + daisy)

    result = weekly_milk
    return result

print(solution())