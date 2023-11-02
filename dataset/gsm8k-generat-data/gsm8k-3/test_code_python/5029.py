def solution():
    """Maria found a store that sells handmade sweaters for $30 and a handmade scarf for $20. She wants to buy one for everyone in her family. She will buy 6 sweaters and 6 scarves. If she has saved $500, how much will be left in her savings after buying all these?"""
    # Define the cost of a sweater and a scarf
    SWEATER_PRICE = 30
    SCARF_PRICE = 20

    # Define the number of sweaters and scarves Maria will buy
    SWEATERS_BOUGHT = 6
    SCARVES_BOUGHT = 6

    # Calculate the total cost of the sweaters
    sweater_cost = SWEATERS_BOUGHT * SWEATER_PRICE

    # Calculate the total cost of the scarves
    scarf_cost = SCARVES_BOUGHT * SCARF_PRICE

    # Calculate the total cost of all the items
    total_cost = sweater_cost + scarf_cost

    # Calculate the amount left in Maria's savings after buying all the items
    remaining_savings = 500 - total_cost

    # Display the amount left in Maria's savings
    result = remaining_savings
    return result

print(solution())