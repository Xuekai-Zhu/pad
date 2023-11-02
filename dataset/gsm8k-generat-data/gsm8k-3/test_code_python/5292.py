def solution():
    """One afternoon, Rachelle, Gretchen and Rocky threw pennies into the fountain and made wishes.  Rachelle threw 180 pennies into the fountain.  Gretchen threw half as many pennies into the fountain as Rachelle and Rocky threw in one-third as many pennies as Gretchen.  What was the total number of pennies thrown into the fountain by the three of them?"""
    # Define the number of pennies Rachelle threw
    rachelle_pennies = 180

    # Calculate the number of pennies Gretchen threw
    gretchen_pennies = rachelle_pennies / 2

    # Calculate the number of pennies Rocky threw
    rocky_pennies = gretchen_pennies / 3

    # Calculate the total number of pennies
    total_pennies = rachelle_pennies + gretchen_pennies + rocky_pennies

    # Display the total number of pennies
    result = total_pennies
    return result

print(solution())