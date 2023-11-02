def solution():
    """A small zoo houses a variety of 68 wild animals. After they send a gorilla family of six to a different zoo, they adopt a hippopotamus from another zoo. A while later, an animal rescue contacted them, and the zoo took in three endangered rhinos. Then one of their lionesses gave birth to cubs, and they opened a meerkat exhibit with twice as many meerkats as they had gained lion cubs. The zoo then had 90 animals in all. How many lion cubs were born at the zoo?"""
    # Starting with 68 animals
    animals = 68

    # Subtract 6 for the gorilla family
    animals -= 6

    # Add 1 for the hippopotamus
    animals += 1

    # Add 3 for the rhinos
    animals += 3

    # Add x for the lion cubs
    # Add 2x meerkats (twice as many as lion cubs)
    animals += x + 2*x

    # Total of 90 animals
    animals = 90

    # Solve for x (number of lion cubs)
    x = (90 - 68 + 6 - 1 - 3) / 3

    # Display the number of lion cubs
    result = x
    return result

print(solution())