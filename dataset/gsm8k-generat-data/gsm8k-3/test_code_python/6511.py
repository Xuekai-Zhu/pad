def solution():
    """On the planet Popton, there are two races of beings: the Hoopits and Neglarts.  Each Hoopit has 3 toes on each of their 4 hands, while each Neglart only has 2 toes on each of their 5 hands. If a Popton automated driverless school bus always carries 7 Hoopit students and 8 Neglart students, how many toes are on the Popton school bus?"""
    # Define the number of toes on each type of being
    HOOPIT_TOES = 3 * 4 * 2  # each Hoopit has 3 toes each on 4 hands
    NEGLART_TOES = 2 * 5 * 8  # each Neglart has 2 toes each on 5 hands

    # Define the number of students on the bus
    hoopit_students = 7
    neglart_students = 8

    # Calculate the total number of toes on the bus
    total_toes = hoopit_students * HOOPIT_TOES + neglart_students * NEGLART_TOES

    # Display the total number of toes
    result = total_toes
    return result

print(solution())