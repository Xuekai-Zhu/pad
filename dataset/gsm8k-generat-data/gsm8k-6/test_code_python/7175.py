def solution():
    # Calculate the number of tadpoles
    number_of_frogs = 5
    number_of_tadpoles = 3 * number_of_frogs

    # Calculate the number of mature frogs
    mature_frogs = (2/3) * number_of_tadpoles

    # Calculate the number of frogs that need to find a new pond
    new_frogs = mature_frogs - number_of_frogs

    if new_frogs > 0:
        result = new_frogs
    else:
        result = 0  # if no new frogs need to find a new pond

    return result

print(solution())