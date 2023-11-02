def solution():
    """There are 40 ducks in a pond. 50 percent of the ducks are Muscovy and 30 percent of the Muscovies are female. How many female Muscovy ducks are there?"""
    
    # Calculate the number of Muscovy ducks
    muscovy_ducks = 40 * 0.5
    
    # Calculate the number of female Muscovy ducks
    female_muscovy = muscovy_ducks * 0.3

    # Display the number of female Muscovy ducks
    result = female_muscovy
    return result

print(solution())