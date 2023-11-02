def solution():
    # Calculate the number of Valentine's day cards Mo needs to buy
    num_cards = int(30 * 0.6)  # Mo wants to give a Valentine to 60% of the 30 students

    # Calculate the total cost of the Valentine's day cards
    total_cost = num_cards * 2

    # Calculate the percentage of his money Mo will spend on Valentine
    percentage_spent = (total_cost / 40) * 100

    result = percentage_spent
    return result

print(solution())