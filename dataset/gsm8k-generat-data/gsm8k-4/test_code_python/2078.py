def solution():
    """There are 40 ducks in a pond. 50 percent of the ducks are Muscovy and 30 percent of the Muscovies are female. How many female Muscovy ducks there?"""
    # Define the total number of ducks and the percentage of Muscovy ducks
    total_ducks = 40
    muscovy_percentage = 0.5

    # Calculate the number of Muscovy ducks and the number of female Muscovy ducks
    muscovy_ducks = total_ducks * muscovy_percentage
    female_muscovy = muscovy_ducks * 0.3

    # Return the result
    result = female_muscovy
    return result

print(solution())