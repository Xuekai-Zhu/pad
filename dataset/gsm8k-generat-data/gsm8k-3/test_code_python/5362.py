def solution():
    """While reading about the history of different towns, Jared learned that Euston had 20 more carriages than Norfolk. Norwich had 100 carriages, and Flying Scotsman had 20 more carriages than Norwich. If Euston had 130 carriages, how many carriages are there in all?"""
    # Define the number of carriages in Norwich
    Norwich_carriages = 100

    # Calculate the number of carriages in Flying Scotsman
    Flying_Scotsman_carriages = Norwich_carriages + 20

    # Define the number of carriages in Euston
    Euston_carriages = 130

    # Calculate the number of carriages in Norfolk
    Norfolk_carriages = Euston_carriages - 20

    # Calculate the total number of carriages
    total_carriages = Norwich_carriages + Flying_Scotsman_carriages + Euston_carriages + Norfolk_carriages

    # Display the total number of carriages
    result = total_carriages
    return result

print(solution())