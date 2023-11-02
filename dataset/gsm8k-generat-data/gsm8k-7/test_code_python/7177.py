def solution():
    gecko_count = 5
    gecko_insect_count = 6
    lizard_count = 3
    lizard_insect_count = gecko_insect_count * 2

    # Calculate the total insects eaten by the geckos
    gecko_total_insects = gecko_count * gecko_insect_count

    # Calculate the total insects eaten by the lizards
    lizard_total_insects = lizard_count * lizard_insect_count

    # Calculate the total insects eaten by all animals
    total_insects = gecko_total_insects + lizard_total_insects
    result = total_insects
    return result

print(solution())