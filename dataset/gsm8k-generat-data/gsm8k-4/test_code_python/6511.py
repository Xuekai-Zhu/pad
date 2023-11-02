def solution():
    """On the planet Popton, there are two races of beings: the Hoopits and Neglarts. Each Hoopit has 3 toes on each of their 4 hands, while each Neglart only has 2 toes on each of their 5 hands. If a Popton automated driverless school bus always carries 7 Hoopit students and 8 Neglart students, how many toes are on the Popton school bus?"""
    # Define the number of Hoopit and Neglart students on the school bus
    hoopit_students = 7
    neglart_students = 8

    # Calculate the total number of toes on the school bus
    hoopit_toes = 3 * 4 * hoopit_students
    neglart_toes = 2 * 5 * neglart_students
    total_toes = hoopit_toes + neglart_toes

    # return the result
    result = total_toes
    return result

print(solution())