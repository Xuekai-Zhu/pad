def solution():
    # Calculate the number of champions who have been women
    women_champions = 0.6 * 25

    # Calculate the number of champions who have been men
    men_champions = 25 - women_champions

    # Calculate the number of men with beards who have been champions
    men_with_beards = 0.4 * men_champions
    result = men_with_beards
    return result

print(solution())