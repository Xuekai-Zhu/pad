def solution():
    total_ducks = 40
    muscovy_percent = 0.5
    female_muscovy_percent = 0.3

    # Calculate the number of Muscovy ducks
    num_muscovies = total_ducks * muscovy_percent

    # Calculate the number of female Muscovy ducks
    num_female_muscovies = num_muscovies * female_muscovy_percent
    result = num_female_muscovies
    return result

print(solution())