def solution():
    """If Raymond does half as much laundry as Sarah, and Sarah does 4 times as much laundry as David, calculate the difference in the amount of laundry Raymond and David do if Sarah does 400 pounds of laundry."""
    sarah_laundry = 400
    david_laundry = sarah_laundry / 4
    raymond_laundry = sarah_laundry / 2
    difference = raymond_laundry - david_laundry
    result = difference
    return result

print(solution())