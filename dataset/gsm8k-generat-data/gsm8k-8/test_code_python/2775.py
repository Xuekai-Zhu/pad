def solution():
    # Define Jack's head circumference
    jack_circumference = 12

    # Calculate Charlie's head circumference
    charlie_circumference = (0.5 * jack_circumference) + 9

    # Calculate Bill's head circumference
    bill_circumference = (2/3) * charlie_circumference

    result = bill_circumference
    return result

print(solution())