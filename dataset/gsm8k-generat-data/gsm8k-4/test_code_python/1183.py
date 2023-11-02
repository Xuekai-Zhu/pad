def solution():
    """A small zoo houses a variety of 68 wild animals. After they send a gorilla family of six to a different zoo, they adopt a hippopotamus from another zoo. A while later, an animal rescue contacted them, and the zoo took in three endangered rhinos. Then one of their lionesses gave birth to cubs, and they opened a meerkat exhibit with twice as many meerkats as they had gained lion cubs. The zoo then had 90 animals in all. How many lion cubs were born at the zoo?"""
    # Define the initial number of animals
    initial_animals = 68

    # Subtract the gorilla family that was sent to another zoo
    remaining_animals = initial_animals - 6

    # Add the hippopotamus they adopted
    remaining_animals += 1

    # Add the three endangered rhinos they took in
    remaining_animals += 3

    # Calculate the total number of meerkats and lion cubs before the meerkat exhibit was opened
    total_meerkats_lions = 90 - remaining_animals

    # Calculate the number of lion cubs that must have been born
    lion_cubs = (total_meerkats_lions / 3) * 2

    # Return the number of lion cubs
    result = lion_cubs
    return result

print(solution())