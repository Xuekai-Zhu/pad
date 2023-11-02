def solution():
    """There are 4 more Muscovy ducks than Cayugas, and 3 more than twice as many Cayugas as Khaki Campbells. If there are 90 ducks total, how many Muscovies are there?"""
    total_ducks = 90
    muscovy_diff = 4
    cayuga_diff = 0
    cayuga_factor = 2
    khaki_campbell = (total_ducks - muscovy_diff - cayuga_diff) / (cayuga_factor + 1)
    cayugas = cayuga_factor * khaki_campbell + cayuga_diff
    muscovies = cayugas + muscovy_diff
    result = muscovies
    return result

print(solution())