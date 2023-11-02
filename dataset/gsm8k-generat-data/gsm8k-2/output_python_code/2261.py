def solution():
    """There are 180 school days in the academic year. Aliyah packs a lunch half the time. Becky packs her lunch half as much as Aliyah. How many days a year does Becky pack her lunch?"""
    total_school_days = 180
    aliyah_packs = total_school_days / 2
    becky_packs = aliyah_packs / 2
    result = becky_packs
    return result

print(solution())