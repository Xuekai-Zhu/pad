def solution():
    # Calculate the total number of alligators
    total_alligators = 2 * 15 / 0.5  # 15 adult females, and half of all alligators are male

    # Calculate the number of female alligators
    female_alligators = total_alligators / 2

    # Calculate the number of juvenile female alligators
    juvenile_female_alligators = female_alligators * 0.4

    # Calculate the number of adult female alligators
    adult_female_alligators = 15

    # Calculate the number of male alligators
    male_alligators = total_alligators - female_alligators
    result = male_alligators
    return result

print(solution())