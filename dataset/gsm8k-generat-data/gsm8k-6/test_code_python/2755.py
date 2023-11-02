def solution():
    # Calculate the number of pencils Bowen buys
    pencils = 40 * (2/5 + 1)  # Bowen buys 2/5 times more pencils than pens

    # Calculate the total cost of the pens and pencils
    cost_pens = 40 * 15  # 40 pens sell at 15 cents each
    cost_pencils = pencils * 25  # pencils sell at 25 cents each
    total_cost = cost_pens + cost_pencils

    result = total_cost
    return result

print(solution())