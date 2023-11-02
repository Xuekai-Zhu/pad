def solution():
    """Josie and her family went on a safari and had an exciting time watching different animals grazing and playing together. She decided to count each animal she saw and calculated their total number. She counted 80 antelopes, 34 more rabbits than antelopes, 42 fewer hyenas than the total number of antelopes and rabbits combined, 50 more wild dogs than hyenas, and the number of leopards was half the number of rabbits. What the total number of animals that Josie counted?"""
    # Define the number of antelopes
    antelopes = 80

    # Calculate the number of rabbits
    rabbits = antelopes + 34

    # Calculate the combined number of rabbits and antelopes
    ra_total = rabbits + antelopes

    # Calculate the number of hyenas
    hyenas = ra_total - 42

    # Calculate the number of wild dogs
    wild_dogs = hyenas + 50

    # Calculate the number of leopards
    leopards = rabbits / 2

    # Calculate the total number of animals counted
    total = antelopes + rabbits + hyenas + wild_dogs + leopards

    # Display the total number of animals counted
    result = total
    return result

print(solution())