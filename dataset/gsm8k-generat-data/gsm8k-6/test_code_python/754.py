def solution():
    # Calculate the cost of the ice cream sundaes
    total_cost = 7.5 + 10 + 8.5 + 9  # the cost of the peanut butter sundae, the Royal banana split sundae, the death by chocolate sundae, and the cherry jubilee sundae
    tip = 0.2 * total_cost  # the tip is 20% of the total cost
    final_bill = total_cost + tip  # the final bill is the total cost plus the tip
    result = final_bill
    return result

print(solution())