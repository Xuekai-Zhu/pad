def solution():
    """Pat's stick is 30 inches long. He covers 7 inches of the stick in dirt. The portion that is not covered in dirt is half as long as Sarah’s stick. Jane’s stick is two feet shorter than Sarah’s stick. How many inches long is Jane’s stick?"""
    pat_stick = 30
    dirt_covered = 7
    sarah_stick = (pat_stick - dirt_covered) * 2
    jane_stick = (sarah_stick - 24) * 12  # 2 feet = 24 inches
    result = jane_stick
    return result

print(solution())