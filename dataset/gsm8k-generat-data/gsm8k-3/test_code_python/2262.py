def solution():
    """There are 180 school days in the academic year. Aliyah packs a lunch half the time. Becky packs her lunch half as much as Aliyah. How many days a year does Becky pack her lunch?"""
    # Define the number of school days and Aliyah's lunch-packing frequency
    SCHOOL_DAYS = 180
    ALIYAH_FREQUENCY = 0.5

    # Calculate how many days Aliyah packs her lunch
    aliyah_days = SCHOOL_DAYS * ALIYAH_FREQUENCY

    # Calculate how many days Becky packs her lunch
    becky_days = aliyah_days * 0.5

    # Display the number of days Becky packs her lunch
    result = becky_days
    return result

print(solution())