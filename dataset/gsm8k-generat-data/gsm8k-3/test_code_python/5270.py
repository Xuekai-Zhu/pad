def solution():
    """Cheryl needs 4 cups of basil to make 1 cup of pesto.  She can harvest 16 cups of basil from her farm every week for 8 weeks.  How many cups of pesto will she be able to make?"""
    # Define the ratio of basil to pesto
    BASIL_TO_PESTO = 4

    # Define the number of weeks and the amount of basil harvested per week
    weeks = 8
    basil_per_week = 16

    # Calculate the total amount of basil harvested over the weeks
    total_basil = weeks * basil_per_week

    # Calculate the number of cups of pesto that can be made with the harvested basil
    pesto_cups = total_basil / BASIL_TO_PESTO

    # Display the number of cups of pesto that can be made
    result = pesto_cups
    return result

print(solution())