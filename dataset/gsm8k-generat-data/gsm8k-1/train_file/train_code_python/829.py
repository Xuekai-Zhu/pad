def solution():
    """Forty percent of the students have elected to learn from home during the pandemic. The remaining students are divided into two equal groups, only one of which is physically in school on any day. What percent of students are present in school?"""
    home_learning_percent = 40
    in_school_percent = (100 - home_learning_percent) / 2
    result = in_school_percent
    return result

print(solution())