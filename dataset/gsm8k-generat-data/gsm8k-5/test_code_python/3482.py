def solution():
    total_cotton_candies = 50  # Cersei bought 50 cotton candies
    candies_given_away = 2 * 5  # Cersei gave away 5 candies each to her brother and sister
    remaining_candies = total_cotton_candies - candies_given_away  # Cersei has these many candies left
    quarter_candies = remaining_candies / 4  # Cersei gives her cousin one-fourth of the remaining candies
    candies_left = quarter_candies - 12  # Cersei ate 12 candies, so these many are left

    result = candies_left
    return result

print(solution())