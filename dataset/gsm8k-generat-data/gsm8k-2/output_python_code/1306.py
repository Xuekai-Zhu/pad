def solution():
    """Sarah's age is equal to three times Mark's age minus 4. Mark is four years older than Billy. Billy is half Ana's age. If Ana will be 15 in 3 years, how old is Sarah?"""
    ana_age = 15 - 3
    billy_age = ana_age / 2
    mark_age = billy_age + 4
    sarah_age = 3 * mark_age - 4
    result = sarah_age
    return result

print(solution())