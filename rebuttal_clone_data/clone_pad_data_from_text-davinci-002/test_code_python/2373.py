def solution():
    total_passengers = 60
    fraction_of_children = 1/4
    number_of_children = total_passengers * fraction_of_children
    number_of_adults = total_passengers - number_of_children
    result = number_of_adults
    return result

print(solution())