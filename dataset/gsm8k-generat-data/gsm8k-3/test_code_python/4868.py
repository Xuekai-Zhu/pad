def solution():
    """
    Ishmael was monitoring whales out at sea for conservation purposes. Each time he takes a trip to sea, he sees
    a different group of whales. On his first trip, he counts 28 male whales and twice as many female whales.
    On his second trip, he sees 8 baby whales, each travelling with their parents. On his third trip,
    he counts half as many male whales as the first trip and the same number of female whales as on the first trip.
    In total, how many whales were out at sea during Ishmael’s monitoring?
    """
    # Define the number of whales Ishmael saw on his first trip
    male_1 = 28
    female_1 = 2 * male_1

    # Define the number of whales Ishmael saw on his second trip
    babies_2 = 8
    parents_2 = 2 * babies_2
    total_2 = babies_2 + parents_2

    # Define the number of whales Ishmael saw on his third trip
    male_3 = male_1 // 2
    female_3 = female_1

    # Calculate the total number of whales
    total_whales = male_1 + female_1 + total_2 + male_3 + female_3

    # Display the total number of whales
    result = total_whales
    return result

print(solution())