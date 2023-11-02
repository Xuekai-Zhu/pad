def solution():
    num_students = 30  # There are 30 students in the class
    percent_to_receive_card = 0.6  # Mo wants to give a Valentine to 60% of the students
    num_cards = num_students * percent_to_receive_card  # Mo needs to buy this many cards
    card_cost = 2  # Each card costs $2
    total_cost = num_cards * card_cost  # Mo will spend this much on cards
    total_budget = 40  # Mo has a budget of $40

    # Calculate the percentage of Mo's budget spent on Valentine cards
    percent_spent = (total_cost / total_budget) * 100
    result = percent_spent
    return result

print(solution())