def solution():
    # Calculate the number of animals in the zoo before any changes
    initial_animals = 68

    # Subtract the gorilla family
    after_gorilla = initial_animals - 6

    # Add the hippopotamus
    after_hippo = after_gorilla + 1

    # Add the rhinos
    after_rhinos = after_hippo + 3

    # Calculate the number of lionesses before the birth
    lionesses = (after_rhinos - 90) * (-1)

    # Calculate the number of lion cubs born
    lion_cubs = (90 - after_rhinos - 2 * lionesses) * (-1)

    result = lion_cubs
    return result

print(solution())