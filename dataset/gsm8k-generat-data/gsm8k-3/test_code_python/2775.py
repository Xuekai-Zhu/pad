def solution():
    """Jack is ordering custom baseball caps for him and his two best friends. Jack's head is 12 inches in circumference. Charlie's head is 9 inches more than half the circumference of Jack's head. Bill's head is 2/3 the circumference of Charlie's head. How many inches in circumference is Bill's head?"""
    # Define Jack's head circumference
    JACK_CIRCUMFERENCE = 12

    # Calculate Charlie's head circumference
    charlie_circumference = (0.5 * JACK_CIRCUMFERENCE) + 9

    # Calculate Bill's head circumference
    bill_circumference = (2/3) * charlie_circumference

    # Display Bill's head circumference
    result = bill_circumference
    return result

print(solution())