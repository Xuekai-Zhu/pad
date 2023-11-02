def solution():
    # Calculate prices of all the dresses
    pauline_dress = 30
    jean_dress = pauline_dress - 10
    ida_dress = jean_dress + 30
    patty_dress = ida_dress + 10

    # Calculate the total amount spent on all dresses
    total_spent = pauline_dress + jean_dress + ida_dress + patty_dress
    result = total_spent
    return result

print(solution())