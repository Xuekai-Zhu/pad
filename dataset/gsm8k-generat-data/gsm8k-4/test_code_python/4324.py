def solution():
    """Carmela has $7 and each of her four cousins has $2. How much will Carmela have to give to each of her cousins so that she and her cousins will have the same amount of money?"""
    # Define Carmela's initial amount of money
    carmela_money = 7

    # Define the cousins' initial amount of money
    cousins_money = 2

    # Calculate the total amount of money among Carmela and her four cousins
    total_money = carmela_money + (4 * cousins_money)

    # Calculate the desired amount of money for each person
    desired_money = total_money / 5

    # Calculate the amount Carmela has to give to each cousin
    to_give = desired_money - cousins_money

    # return the result
    result = to_give
    return result

print(solution())