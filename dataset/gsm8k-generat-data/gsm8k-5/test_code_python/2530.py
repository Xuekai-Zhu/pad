def solution():
    donuts = 3 * 12  # Katie's family eats 3 dozen donuts, which is 3 x 12 = 36 donuts
    coffee_per_donut = 2  # For each donut they need 2 ounces of coffee
    total_coffee_needed = donuts * coffee_per_donut  # Calculate the total amount of coffee needed

    # Calculate the number of pots of coffee needed
    pots_of_coffee = total_coffee_needed / 12
    if total_coffee_needed % 12 != 0:
        pots_of_coffee += 1

    # Calculate the total cost of coffee
    total_coffee_cost = pots_of_coffee * 3
    result = total_coffee_cost
    return result

print(solution())