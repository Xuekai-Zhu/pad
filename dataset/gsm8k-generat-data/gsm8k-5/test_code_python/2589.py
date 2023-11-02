def solution():
    total_apples = 450  # Bob picked 450 apples
    num_children = 33  # There are 33 children in the family
    children_apples = num_children * 10  # Each child ate 10 apples
    adult_apples = total_apples - children_apples  # The remaining apples were eaten by adults
    apples_per_adult = 3  # Each adult ate 3 apples
    num_adults = adult_apples // apples_per_adult  # Divide the total adult apples by the number of apples per adult
    result = num_adults
    return result

print(solution())