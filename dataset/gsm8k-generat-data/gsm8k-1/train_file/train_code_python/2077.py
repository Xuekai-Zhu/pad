def solution():
    """There are 40 ducks in a pond. 50 percent of the ducks are Muscovy and 30 percent of the Muscovies are female. How many female Muscovy ducks are there?"""
    total_ducks = 40
    muscovy_percent = 50
    muscovy_ducks = total_ducks * (muscovy_percent / 100)
    female_percent = 30
    female_muscovy = muscovy_ducks * (female_percent / 100)
    result = female_muscovy
    return result

print(solution())