def solution():
    cost_per_pot = 12  # Françoise buys each pot for €12
    selling_price = cost_per_pot * 1.25  # Françoise sells each pot for 25% higher than the cost
    num_pots_sold = 150  # Françoise sells 150 pots

    # Calculate Françoise's profit from selling the pots
    profit = (selling_price - cost_per_pot) * num_pots_sold

    # Calculate how much Françoise will give back to the association
    donation = profit * 0.8  # Françoise donates 80% of her profit to the association
    result = donation
    return result

print(solution())