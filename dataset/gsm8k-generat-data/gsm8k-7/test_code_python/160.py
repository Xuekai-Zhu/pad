def solution():
    num_people = 4
    burgers_price_per_pound = 3
    burgers_weight = 100
    condiments_and_propane_cost = 80
    john_alcohol_cost = 200

    # Calculate the total cost of burgers
    burgers_cost = burgers_price_per_pound * burgers_weight

    # Calculate the total cost of all items except alcohol
    total_without_alcohol = burgers_cost + condiments_and_propane_cost

    # Calculate the total cost split evenly among all parties
    total_split_cost = total_without_alcohol / num_people

    # Calculate the amount John spent on top of the split cost
    john_extra_cost = john_alcohol_cost - total_split_cost

    # Calculate John's total cost altogether
    john_total_cost = total_split_cost + john_extra_cost
    result = john_total_cost
    return result

print(solution())