def solution():
    male_adults = 100  # There were 100 male adults
    female_adults = male_adults + 50  # There were 50 more female adults than male adults
    total_adults = male_adults + female_adults  # Calculate the total number of adults
    children = 2 * total_adults  # Children were twice the total number of adults
    total_people = male_adults + female_adults + children  # Calculate the total number of people attending the reunion
    result = total_people
    return result

print(solution())