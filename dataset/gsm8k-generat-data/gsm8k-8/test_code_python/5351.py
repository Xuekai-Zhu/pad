def solution():
    # Calculate the total number of patrons
    total_patrons = 12 + 27

    # Calculate the number of golf carts needed
    carts_needed = total_patrons // 3
    if total_patrons % 3 != 0:
        carts_needed += 1

    result = carts_needed
    return result

print(solution())