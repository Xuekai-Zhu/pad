def solution():
    """Jack is ordering custom baseball caps for him and his two best friends. Jack's head is 12 inches in circumference. Charlie's head is 9 inches more than half the circumference of Jack's head. Bill's head is 2/3 the circumference of Charlie's head. How many inches in circumference is Bill's head?"""
    jack_circumference = 12
    charlie_circumference = 9 + 0.5 * jack_circumference
    bill_circumference = 0.67 * charlie_circumference
    result = bill_circumference
    return result

print(solution())