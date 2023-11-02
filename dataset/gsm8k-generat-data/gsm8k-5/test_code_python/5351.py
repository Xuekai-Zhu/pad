def solution():
    total_patrons = 12 + 27  # There are 12 patrons who came in cars and 27 from a bus waiting in the overflow parking lot
    golf_cart_capacity = 3  # Ellen can fit 3 patrons in a golf cart

    # Calculate the total number of golf carts needed to transport all patrons
    golf_carts_needed = (total_patrons // golf_cart_capacity) + (1 if total_patrons % golf_cart_capacity != 0 else 0)

    result = golf_carts_needed
    return result

print(solution())