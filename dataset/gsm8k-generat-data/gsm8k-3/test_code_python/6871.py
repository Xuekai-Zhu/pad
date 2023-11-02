def solution():
    """John raises emu.  He has 4 pens for emu and each pen has 6 emus in it.  Each female emu lays 1 egg per day.  If half the emu are females how many eggs does he get a week?"""
    # Define the number of pens and emus per pen
    PENS = 4
    EMUS_PER_PEN = 6

    # Calculate the total number of emus
    total_emus = PENS * EMUS_PER_PEN

    # Calculate the number of female emus and the number of eggs per day
    female_emus = total_emus // 2
    eggs_per_day = female_emus

    # Calculate the number of eggs per week
    eggs_per_week = eggs_per_day * 7

    # Display the number of eggs per week
    result = eggs_per_week
    return result

print(solution())