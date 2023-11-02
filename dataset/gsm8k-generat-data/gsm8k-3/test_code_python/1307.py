def solution():
    """Sarah's age is equal to three times Mark's age minus 4. Mark is four years older than Billy. Billy is half Ana's age. If Ana will be 15 in 3 years, how old is Sarah?"""
    # Calculate Ana's current age
    ana_age = 15 - 3
    # Calculate Billy's age
    billy_age = ana_age / 2
    # Calculate Mark's age
    mark_age = billy_age + 4
    # Calculate Sarah's age
    sarah_age = 3 * mark_age - 4
    
    result = sarah_age
    return result

print(solution())