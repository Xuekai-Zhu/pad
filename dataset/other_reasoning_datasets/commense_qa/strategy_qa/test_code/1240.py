def solution():
    cheshire_in_uk = True
    la_marseillaise_is_french_anthem = True
    # Check if citizens of Cheshire sing La Marseillaise
    if not (cheshire_in_uk and la_marseillaise_is_french_anthem):
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())