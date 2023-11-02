def solution():
    """At a cafe, the breakfast plate has two eggs and twice as many bacon strips as eggs. If 14 customers order breakfast plates, how many bacon strips does the cook need to fry?"""
    eggs_per_plate = 2
    bacon_per_plate = 2 * eggs_per_plate
    total_plates = 14
    total_bacon_strips = bacon_per_plate * total_plates
    result = total_bacon_strips
    return result

print(solution())