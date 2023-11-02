def solution():
    price_per_pound = 1.6
    price_increase_percentage = 0.25
    num_people = 4
    num_pounds_per_person = 2

    # Calculate the new price per pound after the price increase
    new_price_per_pound = price_per_pound * (1 + price_increase_percentage)

    # Calculate the total cost of 2 pounds of apples per person
    cost_per_person = new_price_per_pound * num_pounds_per_person

    # Calculate the total cost of 2 pounds of apples per person for the entire family
    total_cost = cost_per_person * num_people
    result = total_cost
    return result

print(solution())