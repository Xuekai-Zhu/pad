def solution():
    num_bottles = 20
    bottle_size = 200  # in mL

    # Calculate the total amount of oil in mL
    total_oil = num_bottles * bottle_size

    # Convert mL to L
    total_oil = total_oil / 1000

    result = total_oil
    return result

print(solution())