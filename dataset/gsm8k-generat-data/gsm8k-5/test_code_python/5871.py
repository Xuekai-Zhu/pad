def solution():
    women_haircuts = 1  # Tayzia is getting a Women's haircut
    children_haircuts = 2  # Tayzia's two daughters are getting a Children's haircut
    tip_percent = 0.2  # Tayzia wants to give a 20% tip

    # Calculate the total cost of the haircuts
    total_cost = (women_haircuts * 48) + (children_haircuts * 36)

    # Calculate the amount of the tip
    tip_amount = total_cost * tip_percent

    result = tip_amount
    return result

print(solution())