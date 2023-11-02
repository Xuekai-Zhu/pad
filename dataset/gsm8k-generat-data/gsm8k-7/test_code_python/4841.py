def solution():
    num_years = 25
    percent_women_champions = 0.6
    percent_men_champions = 1 - percent_women_champions
    percent_men_with_beard = 0.4

    # Calculate the total number of champions in the last 25 years
    total_champions = num_years

    # Calculate the number of female champions in the last 25 years
    num_female_champions = total_champions * percent_women_champions

    # Calculate the number of male champions in the last 25 years
    num_male_champions = total_champions * percent_men_champions

    # Calculate the number of male champions with beards in the last 25 years
    num_male_champions_with_beard = num_male_champions * percent_men_with_beard

    result = num_male_champions_with_beard
    return result

print(solution())