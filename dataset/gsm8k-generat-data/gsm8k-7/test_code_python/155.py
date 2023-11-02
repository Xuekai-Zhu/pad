def solution():
    total_mangoes = 60
    sold_to_market = 20
    sold_to_community = (total_mangoes - sold_to_market) / 2
    mangoes_per_kilo = 8

    # Calculate the total number of mangoes remaining
    remaining_mangoes = (total_mangoes - sold_to_market) - sold_to_community

    # Calculate the total number of mangoes in terms of kilos
    remaining_mangoes_kilos = remaining_mangoes / mangoes_per_kilo

    result = remaining_mangoes_kilos
    return result

print(solution())