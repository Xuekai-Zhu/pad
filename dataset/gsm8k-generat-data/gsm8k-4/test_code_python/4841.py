def solution():
    """In the last 25 years, 60% of Scrabble champions have been women and the rest have been men. There is one champion per year. Of the men, 40% had a beard. How many men with beards have been Scrabble champion?"""
    # Define the total number of Scrabble champions in the last 25 years
    total_champions = 25

    # Calculate the number of women champions
    women_champions = total_champions * 0.6

    # Calculate the number of men champions
    men_champions = total_champions - women_champions

    # Calculate the number of men with beards
    men_with_beards = men_champions * 0.4

    # Return the result
    result = men_with_beards
    return result

print(solution())