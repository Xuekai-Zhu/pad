def solution():
    # Calculate the number of bracelets Chantel made in the first five days
    bracelets_made_first_five_days = 2 * 5

    # Calculate the number of bracelets Chantel gave away at school
    bracelets_given_away_school = 3

    # Calculate the number of bracelets Chantel made in the next four days
    bracelets_made_next_four_days = 3 * 4

    # Calculate the number of bracelets Chantel gave away at soccer practice
    bracelets_given_away_soccer = 6

    # Calculate the total number of bracelets Chantel has in the end
    total_bracelets = (bracelets_made_first_five_days - bracelets_given_away_school) + (
                bracelets_made_next_four_days - bracelets_given_away_soccer)

    result = total_bracelets
    return result

print(solution())