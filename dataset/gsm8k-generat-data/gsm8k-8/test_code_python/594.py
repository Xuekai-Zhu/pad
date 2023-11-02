def solution():
    # Define initial number of shells
    initial_shells = 2

    # Calculate the number of shells Ed found
    ed_shells = 7 + 2 + 4

    # Calculate the number of shells Jacob found
    jacob_shells = ed_shells + 2

    # Calculate the total number of shells
    total_shells = initial_shells + ed_shells + jacob_shells

    result = total_shells
    return result

print(solution())