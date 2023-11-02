def solution():
    num_guests = 200
    num_women = 0.4 * num_guests
    num_men = num_guests - num_women
    num_women_with_ears = 0.8 * num_women
    num_men_with_ears = 0.6 * num_men

    total_ears = num_women_with_ears + num_men_with_ears
    result = total_ears
    return result

print(solution())