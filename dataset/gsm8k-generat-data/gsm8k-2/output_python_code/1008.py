def solution():
    """Lagoon island is populated by alligators. Half the alligators are male. The rest are female. Among the females, 40% are juveniles. There are 15 adult females. How many male alligators are there?"""
    total_alligators = 2 * 15  # since half the alligators are male
    num_female = total_alligators - 15
    num_juvenile_female = round(0.4 * num_female)  # rounding to nearest integer
    num_adult_female = 15
    num_male = total_alligators - num_female
    result = num_male
    return result

print(solution())