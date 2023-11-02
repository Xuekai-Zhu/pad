def solution():
    fish_caught_past_months = 80  # Erica caught 80 kg of fish in the past four months
    fish_caught_today = 2 * fish_caught_past_months  # Erica caught twice as many fish as she did in the past four months
    price_per_kg = 20  # Erica sells her fish for $20 per kg

    # Calculate the total amount of money Erica will earn from selling her fish
    total_money_earned = (fish_caught_past_months + fish_caught_today) * price_per_kg

    result = total_money_earned
    return result

print(solution())