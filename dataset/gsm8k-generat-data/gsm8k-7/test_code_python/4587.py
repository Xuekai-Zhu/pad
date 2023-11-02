def solution():
    num_bracelets_day1 = 2
    num_days_day1 = 5
    num_given_away_day1 = 3

    num_bracelets_day2 = 3
    num_days_day2 = 4
    num_given_away_day2 = 6

    # Calculate the total number of bracelets made in the first 5 days
    total_bracelets_day1 = num_bracelets_day1 * num_days_day1

    # Calculate the total number of bracelets made in the next 4 days
    total_bracelets_day2 = num_bracelets_day2 * num_days_day2

    # Calculate the total number of bracelets given away
    total_given_away = num_given_away_day1 + num_given_away_day2

    # Calculate the total number of bracelets Chantel has in the end
    end_total = total_bracelets_day1 + total_bracelets_day2 - total_given_away
    result = end_total
    return result

print(solution())