def solution():
    """
    A small zoo houses a variety of 68 wild animals. After they send a gorilla family of six to a different zoo, 
    they adopt a hippopotamus from another zoo. A while later, an animal rescue contacted them, and the zoo took 
    in three endangered rhinos. Then one of their lionesses gave birth to cubs, and they opened a meerkat exhibit
    with twice as many meerkats as they had gained lion cubs. The zoo then had 90 animals in all. How many lion cubs 
    were born at the zoo?
    """
    initial_animals = 68
    gorilla_family = 6
    hippo = 1
    rhinos = 3
    meerkats = 0
    lion_cubs = 0

    # Calculate current total number of animals
    current_animals = initial_animals - gorilla_family + hippo + rhinos + lion_cubs + meerkats

    # Iterate through possible numbers of lion cubs until total animals equals 90
    while current_animals != 90:
        lion_cubs += 1
        meerkats = 2 * lion_cubs
        current_animals = initial_animals - gorilla_family + hippo + rhinos + lion_cubs + meerkats

    result = lion_cubs
    return result

print(solution())