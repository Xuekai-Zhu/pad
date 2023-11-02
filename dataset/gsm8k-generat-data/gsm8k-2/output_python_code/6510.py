def solution():
    """On the planet Popton, there are two races of beings: the Hoopits and Neglarts. Each Hoopit has 3 toes on each of their 4 hands, while each Neglart only has 2 toes on each of their 5 hands. If a Popton automated driverless school bus always carries 7 Hoopit students and 8 Neglart students, how many toes are on the Popton school bus?"""
    hoopit_toes_per_student = 3 * 4 * 2  # 3 toes on each of 4 hands
    neglart_toes_per_student = 2 * 5 * 2  # 2 toes on each of 5 hands
    total_hoopit_toes = 7 * hoopit_toes_per_student
    total_neglart_toes = 8 * neglart_toes_per_student
    total_toes = total_hoopit_toes + total_neglart_toes
    result = total_toes
    return result

print(solution())