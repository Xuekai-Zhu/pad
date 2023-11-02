def solution():
    """The Dark Lord needs to transport 1200 pounds of swords to the Enchanted Forest for a battle with the elves. He has 10 squads of 8 orcs each. How many pounds of swords does each orc have to carry?"""
    # Define the total number of orcs
    total_orcs = 10 * 8

    # Calculate the amount of swords each orc has to carry
    swords_per_orc = 1200 / total_orcs

    # Display the amount of swords each orc has to carry
    result = swords_per_orc
    return result

print(solution())