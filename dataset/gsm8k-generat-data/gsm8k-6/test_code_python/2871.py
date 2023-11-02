def solution():
    # Calculate the total amount of money Gloria can raise from selling her trees
    cypress_money = 20 * 100  # $100 for each cypress tree
    maple_money = 24 * 300  # $300 for each maple tree
    pine_money = 600 * 200  # $200 for each pine tree
    total_money = cypress_money + maple_money + pine_money

    # Calculate the amount of money Gloria will have left after buying the cabin
    remaining_money = total_money - 129000 + 150  # $150 in cash

    result = remaining_money
    return result

print(solution())