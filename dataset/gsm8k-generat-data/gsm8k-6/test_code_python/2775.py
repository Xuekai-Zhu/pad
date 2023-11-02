def solution():
    # Calculate the circumference of Jack's head
    jack_circumference = 12

    # Calculate the circumference of Charlie's head
    charlie_circumference = 9 + 0.5 * jack_circumference

    # Calculate the circumference of Bill's head
    bill_circumference = (2/3) * charlie_circumference

    result = bill_circumference
    return result

print(solution())