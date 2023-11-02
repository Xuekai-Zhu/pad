def solution():
    """There are 4 more Muscovy ducks than Cayugas, and 3 more than twice as many Cayugas as Khaki Campbells. If there are 90 ducks total, how many Muscovies are there?"""
    # Let x be the number of Khaki Campbells
    # Then there are 2x+3 Cayugas and 2x+3+4=2x+7 Muscovy ducks
    # The total number of ducks is x+2x+3+2x+7=5x+10=90
    # Solving for x, we get x=16
    # Therefore, there are 2x+7=39 Muscovy ducks
    muscovy_ducks = 2*16+7
    result = muscovy_ducks
    return result

print(solution())