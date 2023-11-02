def solution():
    """Saheed made four times as much money as Kayla. Kayla made $30 less than Vika. Vika made $84. How many dollars did Saheed make?"""
    # Define the initial amount made by Vika
    vika_money = 84

    # Calculate the amount made by Kayla
    kayla_money = vika_money - 30

    # Calculate the amount made by Saheed
    saheed_money = kayla_money * 4

    # return the result
    result = saheed_money
    return result

print(solution())