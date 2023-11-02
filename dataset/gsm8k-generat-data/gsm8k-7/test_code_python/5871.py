def solution():
    num_women = 1
    women_price = 48

    num_children = 2
    children_price = 36

    tip_percent = 0.2  # 20% tip

    # Calculate the total cost of all haircuts
    total_cost = (num_women * women_price) + (num_children * children_price)

    # Calculate the tip amount
    tip_amount = total_cost * tip_percent

    result = tip_amount
    return result

print(solution())