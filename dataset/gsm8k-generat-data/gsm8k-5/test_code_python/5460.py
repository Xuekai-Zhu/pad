def solution():
    initial_coffee = 12  # Omar buys a 12-ounce cup of coffee
    first_drink = initial_coffee / 4  # Omar drinks one-quarter of the cup on the way to work
    second_drink = initial_coffee / 2  # Omar drinks half of the cup when he gets to his office
    remaining_coffee = initial_coffee - first_drink - second_drink  # Omar forgets to drink any more of his coffee
    last_drink = 1  # Omar drinks 1 ounce of the remaining amount

    # Calculate the final amount of coffee left in the cup
    final_coffee = remaining_coffee - last_drink
    result = final_coffee
    return result

print(solution())