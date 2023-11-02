def solution():
    """Maria found a store that sells handmade sweaters for $30 and a handmade scarf for $20. She wants to buy one for everyone in her family. She will buy 6 sweaters and 6 scarves. If she has saved $500, how much will be left in her savings after buying all these?"""
    # Define the prices of sweaters and scarves
    sweater_price = 30
    scarf_price = 20

    # Calculate the total cost of buying 6 sweaters and 6 scarves
    total_cost = (6 * sweater_price) + (6 * scarf_price)

    # Calculate the amount left in Maria's savings after buying all items
    remaining_savings = 500 - total_cost

    # return the result
    result = remaining_savings
    return result

print(solution())