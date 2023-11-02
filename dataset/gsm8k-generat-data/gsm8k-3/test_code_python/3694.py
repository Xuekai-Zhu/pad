def solution():
    """For many years, the number of sharks in Pelican Bay has been twice the number of Pelicans in Shark Bite Cove. But today scientists say one-third of the Pelicans in Shark Bite Cove have moved to Pelican Bay. If there are still 60 sharks in Pelican Bay, how many Pelicans remain in Shark Bite Cove?"""
    # Let's assume there are 'x' Pelicans in Shark Bite Cove
    # Then the number of sharks in Pelican Bay is 2x (since it's twice the number of Pelicans)

    # Let's calculate the number of Pelicans that moved to Pelican Bay
    pelicans_moved = x/3

    # After the Pelicans moved, the number of Pelicans in Shark Bite Cove is reduced to x - pelicans_moved
    # And the number of sharks in Pelican Bay is still 60
    # So we can write the equation: 60 = 2(x - pelicans_moved)

    # Simplifying the equation, we get:
    # 30 = x - pelicans_moved
    # pelicans_moved = x - 30

    # Substituting this value of pelicans_moved in the first equation, we get:
    # 60 = 2x - 2(x - 30)
    # 60 = 2x - 2x + 60
    # 2x = 120
    # x = 60

    # So there were initially 60 Pelicans in Shark Bite Cove
    # And after one-third of them moved to Pelican Bay, there are 40 Pelicans remaining in Shark Bite Cove
    result = 40
    return result

print(solution())