def solution():
    """Each member of Greg’s softball team needs to buy one uniform made up of a shirt, a pair of pants, and socks. A shirt costs $7.50, a pair of pants cost $15, and socks cost $4.50 each if each team member buys the uniform items on their own. If they buy the items as a group, they are given a discount. A discounted shirt cost $6.75, a discounted pair of pants cost $13.50, and discounted socks cost $3.75. How much would their team of 12 save with the group discount?"""
    # Define the prices for each item
    shirt_price = 7.5
    pants_price = 15
    socks_price = 4.5

    # Define the discounted prices for each item
    discounted_shirt_price = 6.75
    discounted_pants_price = 13.5
    discounted_socks_price = 3.75

    # Calculate the total cost of each uniform without discount
    total_cost_without_discount = shirt_price + pants_price + socks_price

    # Calculate the total cost of each uniform with discount
    total_cost_with_discount = discounted_shirt_price + discounted_pants_price + discounted_socks_price

    # Calculate the amount saved for each uniform by using discount
    amount_saved_per_uniform = total_cost_without_discount - total_cost_with_discount

    # Calculate the total amount saved by the team
    total_amount_saved = amount_saved_per_uniform * 12

    result = total_amount_saved
    return result

print(solution())