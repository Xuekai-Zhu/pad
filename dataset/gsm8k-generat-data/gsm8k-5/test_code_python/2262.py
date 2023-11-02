def solution():
    school_days = 180  # There are 180 school days in the academic year

    # Aliyah packs her lunch half the time
    aliyah_lunch_days = school_days / 2

    # Becky packs her lunch half as much as Aliyah
    becky_lunch_days = aliyah_lunch_days / 2

    result = becky_lunch_days
    return result

print(solution())