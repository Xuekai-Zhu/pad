def solution():
    num_potato_chips_bags = 3
    potato_chips_bag_price = 1.0
    creme_fraiche_price = 5.0
    caviar_price = 73.0
    num_people = 3

    # Calculate the total cost of all potato chip bags
    total_potato_chips_cost = num_potato_chips_bags * potato_chips_bag_price

    # Calculate the total cost of the creme fraiche and caviar
    total_creme_fraiche_and_caviar_cost = creme_fraiche_price + caviar_price

    # Calculate the total cost of the appetizer
    total_cost = total_potato_chips_cost + total_creme_fraiche_and_caviar_cost

    # Calculate the cost per person
    cost_per_person = total_cost / num_people
    result = cost_per_person
    return result

print(solution())