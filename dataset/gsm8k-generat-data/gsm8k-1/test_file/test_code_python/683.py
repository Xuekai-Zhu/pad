def solution():
    """There is one set of twins and one set of triplets. One twin is 7 years older than one triplet. If their combined ages are 44, how old is one of the twins?"""
    total_age = 44
    twin_age_difference = 7
    # Let's assume the age of one of the triplets to be x
    # So, the age of the older twin would be x + twin_age_difference
    # Age of the other twin and the other triplet would be the same as the first twin and triplet
    age_sum = (x + (x + twin_age_difference)) + (3*x)  # total age of all four siblings
    # We know that age_sum = total_age, so we can solve for x and then find the age of one of the twins
    x = (total_age - twin_age_difference) / 4
    twin_age = x + twin_age_difference
    result = twin_age
    return result

print(solution())