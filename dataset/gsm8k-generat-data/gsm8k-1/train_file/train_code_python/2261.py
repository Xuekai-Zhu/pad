def solution():
    """There are 180 school days in the academic year. Aliyah packs a lunch half the time. Becky packs her lunch half as much as Aliyah. How many days a year does Becky pack her lunch?"""
    school_days = 180
    aliyah_lunches = school_days / 2
    becky_lunches = aliyah_lunches / 2
    result = becky_lunches
    return result

print(solution())