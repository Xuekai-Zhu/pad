def solution():
    pencils = 6
    pens = 2 * pencils
    erasers = 1
    total_items = pencils + pens + erasers
    if total_items != 13:
        return "There is an error in the calculation"
    result = pencils
    return result

print(solution())