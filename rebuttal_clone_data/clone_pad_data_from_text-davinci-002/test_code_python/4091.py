def solution():
    even_number_of_people = True
    men = 4
    women = 6
    percentage_of_women = 20
    number_of_people = men + women
    total_people = number_of_people / (1 - (percentage_of_women / 100))
    result = total_people
    return result

print(solution())