def solution():
    # Calculate the total number of patrons in the overflow parking lot
    total_patrons = 12 + 27

    # Calculate the number of golf carts needed to transport all the patrons
    carts_needed = total_patrons // 3  # integer division will give the number of golf carts needed
    if total_patrons % 3 != 0:  # if there are some remaining patrons, one more golf cart is needed
        carts_needed += 1

    result = carts_needed
    return result

print(solution())