def solution():
    """There are 4 more Muscovy ducks than Cayugas, and 3 more than twice as many Cayugas as Khaki Campbells. If there are 90 ducks total, how many Muscovies are there?"""
    # Define the number of Khaki Campbells ducks
    khaki_campbells = None

    # Define the number of Cayugas ducks
    cayugas = (khaki_campbells * 2) + 3

    # Define the number of Muscovy ducks
    muscovy = cayugas + 4

    # Define the total number of ducks
    total_ducks = 90

    # Solve the system of equations to determine the number of Khaki Campbells ducks
    # x + y + z = total_ducks
    # z = y + 4
    # y = 2x + 3
    # Substituting y and z into the first equation:
    # x + (2x+3) + ((2x+3)+4) = total_ducks
    # 5x + 10 = total_ducks
    # x = (total_ducks - 10) / 5
    khaki_campbells = (total_ducks - 10) / 5

    # Calculate the number of Muscovy ducks
    muscovy = cayugas + 4

    # return the result
    result = muscovy
    return result

print(solution())