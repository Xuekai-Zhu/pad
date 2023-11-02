def solution():
    population = 974000  # Population of Delaware is 974,000
    phones_per_1000 = 673  # Study showed there are 673 cell phones per 1000 people in the state

    # Calculate the total number of cell phones in Delaware
    total_phones = population * phones_per_1000 / 1000
    result = total_phones
    return result

print(solution())