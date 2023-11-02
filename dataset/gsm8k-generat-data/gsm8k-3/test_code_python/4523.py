def solution():
    """An alien invades Earth.  It abducts 200 people.  He returns 80% of the people abducted.  After that he takes 10 people to another planet.  He took the rest to his home planet.  How many people did he take to his home planet?"""
    # Define the number of people abducted
    people_abducted = 200

    # Calculate the number of people returned
    people_returned = people_abducted * 0.8

    # Calculate the number of people taken to another planet
    people_to_another_planet = 10

    # Calculate the number of people taken to the home planet
    people_to_home_planet = people_abducted - people_returned - people_to_another_planet

    # Display the number of people taken to the home planet
    result = people_to_home_planet
    return result

print(solution())