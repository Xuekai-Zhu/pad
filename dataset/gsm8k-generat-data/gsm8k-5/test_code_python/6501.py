def solution():
    starting_clothes = 100  # Amara started with 100 pieces of clothing
    donated_first_home = 5  # She donated 5 clothes to the first orphanage home
    donated_second_home = 3 * donated_first_home  # She tripled the donation to the second orphanage home
    thrown_away = 15  # She threw away 15 pieces of clothing

    # Calculate the remaining number of pieces of clothing
    remaining_clothes = starting_clothes - donated_first_home - donated_second_home - thrown_away
    result = remaining_clothes
    return result

print(solution())