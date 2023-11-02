def solution():
    """John raises emu. He has 4 pens for emu and each pen has 6 emus in it. Each female emu lays 1 egg per day. If half the emu are females how many eggs does he get a week?"""
    # Define the number of pens and emus per pen
    pens = 4
    emus_per_pen = 6

    # Calculate the total number of emus
    total_emus = pens * emus_per_pen

    # Calculate the number of female emus
    female_emus = total_emus / 2

    # Calculate the number of eggs laid per day
    eggs_per_day = female_emus

    # Calculate the number of eggs laid per week
    eggs_per_week = eggs_per_day * 7

    # return the result
    result = eggs_per_week
    return result

print(solution())