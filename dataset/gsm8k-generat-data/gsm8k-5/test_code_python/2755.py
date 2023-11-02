def solution():
    pens_price = 0.15  # Price of one pen in dollars
    pencils_price = 0.25  # Price of one pencil in dollars
    num_pens = 40  # Bowen buys 40 pens
    num_pencils = round(num_pens * 2/5 * 10) / 10  # Bowen buys 2/5 more pencils than pens (round to nearest tenth)

    # Calculate the total cost of pens and pencils
    pens_cost = num_pens * pens_price
    pencils_cost = num_pencils * pencils_price
    total_cost = pens_cost + pencils_cost
    result = total_cost
    return result

print(solution())