def solution():
    initial_amount = 65
    spent_on_ice_cream = 5

    # Calculate the remaining amount of money after buying ice cream
    remaining_amount = initial_amount - spent_on_ice_cream

    # Calculate the amount spent on the t-shirt
    spent_on_tshirt = remaining_amount / 2

    # Calculate the remaining amount after buying the t-shirt
    remaining_amount = remaining_amount - spent_on_tshirt

    # Calculate the amount Lulu deposited in the bank
    deposited_amount = remaining_amount / 5

    # Calculate the final amount left with Lulu
    remaining_amount = remaining_amount - deposited_amount
    result = remaining_amount
    return result

print(solution())