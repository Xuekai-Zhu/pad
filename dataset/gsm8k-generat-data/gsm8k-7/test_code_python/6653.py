def solution():
    cups_of_sugar_at_home = 3
    num_bags_of_sugar = 2
    cups_of_sugar_per_bag = 6
    cups_of_sugar_per_batch = 1*2  # 1 cup for batter, 2 cups for frosting
    cupcakes_per_batch = 12

    # Calculate the total cups of sugar
    total_cups_of_sugar = cups_of_sugar_at_home + (num_bags_of_sugar * cups_of_sugar_per_bag)

    # Calculate the total batches of cupcakes that can be made
    total_batches = int(total_cups_of_sugar / cups_of_sugar_per_batch)

    # Calculate the total dozens of cupcakes that can be made
    total_dozens = total_batches * cupcakes_per_batch / 12
    result = total_dozens
    return result

print(solution())