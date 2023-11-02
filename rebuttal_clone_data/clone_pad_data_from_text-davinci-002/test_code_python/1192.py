def solution():
    attendees = 120
    fraction_men = 1/3
    fraction_women = 1/2
    fraction_children = 1 - (fraction_men + fraction_women)
    number_children = attendees * fraction_children
    result = number_children
    
    return result

print(solution())