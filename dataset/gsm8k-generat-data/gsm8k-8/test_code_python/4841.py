def solution():
    # Calculate the number of women champions in 25 years
    women_champions = int(0.6 * 25)

    # Calculate the number of men champions in 25 years
    men_champions = 25 - women_champions

    # Calculate the number of men with beards who were champions
    men_with_beards = int(0.4 * men_champions)

    result = men_with_beards
    return result

print(solution())