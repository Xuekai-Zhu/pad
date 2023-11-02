def solution():
    # Compute the number of bracelets made in the first 5 days
    bracelets_made_first_5_days = 2 * 5

    # Compute the number of bracelets made in the next 4 days
    bracelets_made_next_4_days = 3 * 4

    # Compute the total number of bracelets made
    total_bracelets_made = bracelets_made_first_5_days + bracelets_made_next_4_days

    # Compute the number of bracelets given away
    bracelets_given_away = 3 + 6

    # Compute the number of bracelets Chantel has at the end
    final_bracelet_count = total_bracelets_made - bracelets_given_away

    result = final_bracelet_count
    return result

print(solution())