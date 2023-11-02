def solution():
    """There are 180 school days in the academic year. Aliyah packs a lunch half the time. Becky packs her lunch half as much as Aliyah. How many days a year does Becky pack her lunch?"""
    # Define the total number of school days
    total_school_days = 180

    # Calculate the number of days Aliyah packs her lunch
    aliyah_packs = total_school_days / 2

    # Calculate the number of days Becky packs her lunch
    becky_packs = aliyah_packs / 2

    # return the result
    result = becky_packs
    return result

print(solution())