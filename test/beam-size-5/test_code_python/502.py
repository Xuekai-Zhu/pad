def solution():
    num_dogs = 6
    num_legs_per_dog = 4
    snowshoe_price = 12.0

    # Calculate the total number of legs needed for all dogs
    total_legs = num_dogs * num_legs_per_dog

    # Calculate the total number of snowshoes needed for all dogs
    total_snowshoes = total_legs * snowshoe_price
    result = total_snowshoes
    return result

print(solution())