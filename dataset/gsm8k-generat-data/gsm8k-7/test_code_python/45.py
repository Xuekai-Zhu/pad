def solution():
    unicorn_pinata_cost = 13
    num_bags_reeses = 4
    cost_per_bag_reeses = 9
    num_bags_snickers = 3
    cost_per_bag_snickers = 5
    num_bags_skittles = 5
    cost_per_bag_skittles = 7

    # Calculate the total cost of all Reese's bags
    total_cost_reeses = num_bags_reeses * cost_per_bag_reeses

    # Calculate the total cost of all Snickers bags
    total_cost_snickers = num_bags_snickers * cost_per_bag_snickers

    # Calculate the total cost of all Skittles bags
    total_cost_skittles = num_bags_skittles * cost_per_bag_skittles

    # Calculate the total cost of the unicorn piñata and all treats
    total_cost = unicorn_pinata_cost + total_cost_reeses + total_cost_snickers + total_cost_skittles
    result = total_cost
    return result

print(solution())