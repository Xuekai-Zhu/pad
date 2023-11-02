def solution():
    # Calculate Ana's current age
    ana_age = 15 - 3  # Ana will be 15 in 3 years

    # Calculate Billy's current age
    billy_age = ana_age / 2

    # Calculate Mark's current age
    mark_age = billy_age + 4  # Mark is four years older than Billy

    # Calculate Sarah's current age
    sarah_age = 3 * mark_age - 4  # Sarah's age is equal to three times Mark's age minus 4

    return sarah_age

print(solution())