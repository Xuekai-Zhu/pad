def solution():
    """On the planet Popton, there are two races of beings: the Hoopits and Neglarts. Each Hoopit has 3 toes on each of their 4 hands, while each Neglart only has 2 toes on each of their 5 hands. If a Popton automated driverless school bus always carries 7 Hoopit students and 8 Neglart students, how many toes are on the Popton school bus?"""
    hoopit_toes_per_hand = 3
    neglart_toes_per_hand = 2
    hoopit_hands = 4
    neglart_hands = 5
    hoopits_on_bus = 7
    neglarts_on_bus = 8
    total_hoopit_toes = hoopit_toes_per_hand * hoopit_hands * hoopits_on_bus
    total_neglart_toes = neglart_toes_per_hand * neglart_hands * neglarts_on_bus
    total_toes = total_hoopit_toes + total_neglart_toes
    result = total_toes
    return result

print(solution())