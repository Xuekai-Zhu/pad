def solution():
    # Calculate the total number of people in the family
    total_people = 3 + 7  # three adults and seven children

    # Calculate the total number of eggs eaten by the adults
    eggs_adults = 3 * 3  # each adult got three eggs

    # Calculate the total number of eggs eaten by the girls
    eggs_girls = 7  # each girl got one egg

    # Calculate the total number of eggs eaten by the boys
    eggs_boys = 12 - eggs_girls  # each boy got one more egg than each girl

    # Calculate the number of boys who went on the trip
    boys = eggs_boys // 2  # each boy ate two eggs

    result = boys
    return result

print(solution())