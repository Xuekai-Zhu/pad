def solution():
    """Mary and Jay are planning a wedding. Of the 240 guests, 60 percent are female.  Of the females, 50 percent are from Jay's family.  How many female guests are from Jay's family?"""
    # Define the total number of guests and the percentage of females
    total_guests = 240
    female_percentage = 0.6

    # Calculate the number of female guests
    female_guests = total_guests * female_percentage

    # Calculate the number of female guests from Jay's family
    jays_female_guests = female_guests * 0.5

    # Display the number of female guests from Jay's family
    result = jays_female_guests
    return result

print(solution())