def solution():
    cabin_price = 129000  # Alfonso is selling the cabin for $129,000
    cash_on_hand = 150  # Gloria has $150 in cash

    # Calculate the total amount Gloria can raise by selling her trees
    cypress_sale = 20 * 100  # Gloria can sell 20 cypress trees for $100 each
    maple_sale = 24 * 300  # Gloria can sell 24 maple trees for $300 each
    pine_sale = 600 * 200  # Gloria can sell 600 pine trees for $200 each
    total_sale = cypress_sale + maple_sale + pine_sale

    # Calculate the amount Gloria will have left after buying the cabin
    remaining_amount = total_sale + cash_on_hand - cabin_price
    result = remaining_amount
    return result

print(solution())