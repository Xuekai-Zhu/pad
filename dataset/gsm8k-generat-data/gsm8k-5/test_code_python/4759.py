def solution():
    old_barbell_cost = 250  # James' old barbell cost $250
    percent_increase = 0.3  # The new barbell costs 30% more than the old one

    # Calculate the cost of the new barbell
    new_barbell_cost = old_barbell_cost + (old_barbell_cost * percent_increase)
    result = new_barbell_cost
    return result

print(solution())