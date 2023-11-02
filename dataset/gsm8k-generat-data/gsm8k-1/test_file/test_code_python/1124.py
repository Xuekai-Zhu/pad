def solution():
    """Liam is 16 years old now. Two years ago, Liam’s age was twice the age of Vince. How old is Vince now?"""
    liam_age_now = 16
    years_ago = 2
    twice_vince_age = liam_age_now - years_ago
    vince_age_now = twice_vince_age / 2
    result = vince_age_now
    return result

print(solution())