def solution():
    sweater_price = 30  # Each handmade sweater costs $30
    scarf_price = 20  # Each handmade scarf costs $20
    num_sweaters = 6  # Maria wants to buy 6 sweaters
    num_scarves = 6  # Maria wants to buy 6 scarves
    total_cost = (sweater_price * num_sweaters) + (scarf_price * num_scarves)  # Calculate the total cost of the items

    # Calculate how much Maria will have left in her savings after buying all the items
    remaining_money = 500 - total_cost
    result = remaining_money
    return result

print(solution())