def solution():
    """There are 4 more Muscovy ducks than Cayugas, and 3 more than twice as many Cayugas as Khaki Campbells. If there are 90 ducks total, how many Muscovies are there?"""
    total_ducks = 90
    cayugas = (total_ducks - 3) / 3
    muscovies = cayugas + 4
    result = muscovies
    return result

print(solution())