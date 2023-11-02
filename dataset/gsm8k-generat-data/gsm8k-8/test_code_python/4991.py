def solution():
    # Calculate total number of boys in school
    total_boys = 0.6 * 200

    # Calculate total number of girls in school
    total_girls = 200 - total_boys

    # Calculate the number of male votes June needs to win
    male_votes_needed = 0.5 * 200 - 0.675 * total_boys

    # Calculate the total number of votes needed to win
    total_votes_needed = 0.5 * 200

    # Calculate the number of female votes June needs to win
    female_votes_needed = total_votes_needed - male_votes_needed

    # Calculate the percentage of female votes June needs to win
    female_percentage_needed = (female_votes_needed / total_girls) * 100

    result = female_percentage_needed
    return result

print(solution())