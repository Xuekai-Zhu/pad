def solution():
    full_container = 2000  # 2-liter container of milk contains 2000 ml of milk
    portion_size = 200  # Each portion of milk is 200 ml

    # Calculate the number of portions Jasmine can pour
    portions = full_container // portion_size
    result = portions
    return result

print(solution())