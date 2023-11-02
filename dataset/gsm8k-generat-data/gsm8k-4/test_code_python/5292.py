def solution():
    """One afternoon, Rachelle, Gretchen and Rocky threw pennies into the fountain and made wishes. Rachelle threw 180 pennies into the fountain. Gretchen threw half as many pennies into the fountain as Rachelle and Rocky threw in one-third as many pennies as Gretchen. What was the total number of pennies thrown into the fountain by the three of them?"""
    # Define the number of pennies thrown by Rachelle
    pennies_rachelle = 180

    # Calculate the number of pennies thrown by Gretchen
    pennies_gretchen = pennies_rachelle / 2

    # Calculate the number of pennies thrown by Rocky
    pennies_rocky = pennies_gretchen / 3

    # Calculate the total number of pennies thrown by all three
    total_pennies = pennies_rachelle + pennies_gretchen + pennies_rocky

    # return the result
    result = total_pennies
    return result

print(solution())