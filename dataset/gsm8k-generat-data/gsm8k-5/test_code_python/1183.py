def solution():
    total_animals = 90  # The zoo has 90 animals in all
    initial_animals = 68  # The zoo starts with 68 wild animals
    gorilla_family = 6  # The zoo sends a gorilla family of six to a different zoo
    hippo = 1  # The zoo adopts a hippopotamus from another zoo
    rhinos = 3  # The zoo takes in three endangered rhinos
    meerkats = 2  # The meerkat exhibit has twice as many meerkats as lion cubs

    # Calculate the total number of animals added to the zoo
    added_animals = gorilla_family + hippo + rhinos + meerkats
    final_animals = initial_animals + added_animals  # Calculate the final number of animals at the zoo

    # Calculate the number of lion cubs born at the zoo
    lions = total_animals - final_animals
    result = lions
    return result

print(solution())