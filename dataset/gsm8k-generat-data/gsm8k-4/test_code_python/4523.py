def solution():
    """An alien invades Earth. It abducts 200 people. He returns 80% of the people abducted. After that he takes 10 people to another planet. He took the rest to his home planet. How many people did he take to his home planet?"""
    # Define the number of people initially abducted
    initial_abduction = 200

    # Calculate the number of people returned to Earth
    return_to_earth = initial_abduction * 0.8

    # Calculate the number of people taken to another planet
    other_planet = 10

    # Calculate the number of people taken to the alien's home planet
    home_planet = initial_abduction - return_to_earth - other_planet

    # Return the result
    result = home_planet
    return result

print(solution())