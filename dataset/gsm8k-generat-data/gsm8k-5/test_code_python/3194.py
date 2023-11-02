def solution():
    total_guests = 1000
    married_percentage = 0.3
    single_percentage = 0.5

    married_guests = married_percentage * total_guests
    single_guests = single_percentage * total_guests
    children_guests = total_guests - married_guests - single_guests

    difference = married_guests - children_guests
    result = difference
    return result

print(solution())