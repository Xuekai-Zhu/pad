def solution():
    population = 974000
    phones_per_thousand = 673

    # Calculate the total number of phones in the state
    total_phones = population * phones_per_thousand / 1000
    result = total_phones
    return result

print(solution())