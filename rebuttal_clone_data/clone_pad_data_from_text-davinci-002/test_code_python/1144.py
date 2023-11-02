def solution():
    age_older_brother = 2 * age_middle_brother - 1
    age_younger_brother = 1/3 * age_older_brother
    total_age = age_older_brother + age_middle_brother + age_younger_brother
    result = total_age
    return result

print(solution())