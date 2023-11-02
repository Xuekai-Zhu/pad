def solution():
    """Jonah decided to set up an aquarium. He started with 14 small fish. He added 2 more, but they ate 6 of his original fish before he could remove them and take them back to the store. He exchanged them for 3 new fish. How many fish does Jonah have now?"""
    # Define the initial number of fish
    initial_fish = 14

    # Calculate the number of fish remaining after the first 2 ate 6
    remaining_fish = initial_fish - 6

    # Add the 2 additional fish
    total_fish = remaining_fish + 2

    # Exchange the 2 fish for 3 new fish
    total_fish += 3

    # Display the total number of fish
    result = total_fish
    return result

print(solution())