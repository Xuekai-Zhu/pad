def solution():
    """Carmela has $7 and each of her four cousins has $2. How much will Carmela have to give to each of her cousins so that she and her cousins will have the same amount of money?"""
    # Define the initial amounts of money
    carmela_money = 7
    cousin_money = 2
    num_cousins = 4

    # Calculate the total amount of money available
    total_money = carmela_money + (cousin_money * num_cousins)

    # Calculate the amount of money each person should have
    equal_money = total_money / (num_cousins + 1)

    # Calculate the amount Carmela needs to give to each cousin
    amount_to_give = equal_money - cousin_money

    # Display the amount Carmela needs to give to each cousin
    result = amount_to_give
    return result

print(solution())