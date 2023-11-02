def solution():
    """Forty percent of the students have elected to learn from home during the pandemic. The remaining students are divided into two equal groups, only one of which is physically in school on any day. What percent of students are present in school?"""
    percentage_home = 40
    percentage_in_school = (100 - percentage_home) / 2
    result = percentage_in_school
    return result

print(solution())