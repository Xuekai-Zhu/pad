def solution():
    cups_per_day = 2  # Luna is supposed to eat 2 cups of kibble every day
    starting_cups = 12  # A new bag of kibble contains 12 cups
    mary_cups = 1 + 1  # Mary gave Luna 1 cup of kibble in the morning and evening
    frank_cups = 1 + 2 * 1  # Frank gave Luna 1 cup in the afternoon and twice as much in the evening

    # Calculate the total cups of kibble Luna ate in one day
    total_cups = mary_cups + frank_cups

    # Calculate the cups of kibble left in the bag
    cups_left = starting_cups - total_cups
    result = cups_left
    return result

print(solution())