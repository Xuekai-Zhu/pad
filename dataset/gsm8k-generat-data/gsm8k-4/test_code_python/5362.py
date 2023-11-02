def solution():
    """While reading about the history of different towns, Jared learned that Euston had 20 more carriages than Norfolk. Norwich had 100 carriages, and Flying Scotsman had 20 more carriages than Norwich. If Euston had 130 carriages, how many carriages are there in all?"""
    # Define the initial number of carriages in Norfolk
    norfolk_carriages = None

    # Calculate the number of carriages in Euston
    euston_carriages = 130

    # Calculate the number of carriages in Norwich
    norwich_carriages = 100

    # Calculate the number of carriages in Flying Scotsman
    flying_scotsman_carriages = norwich_carriages + 20

    # Calculate the number of carriages in Norfolk
    norfolk_carriages = euston_carriages - 20

    # Calculate the total number of carriages
    total_carriages = norfolk_carriages + norwich_carriages + flying_scotsman_carriages + euston_carriages

    result = total_carriages
    return result

print(solution())