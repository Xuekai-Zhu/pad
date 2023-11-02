def solution():
    # Calculate the total amount of paint used in the 1 : 2 : 5 ratio
    total_paint = 1 + 2 + 5  # ratio of blue : green : white
    # Calculate the amount of green paint used in the ratio
    green_paint = 2/8  # 2 parts green paint in a total of 8 parts paint
    # Determine how many gallons of paint are total using a proportion
    gallons_total = (6 / green_paint) * total_paint
    result = gallons_total
    return result

print(solution())