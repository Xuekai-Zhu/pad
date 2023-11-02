def solution():
    # Let's assume bobby's age is b
    # Then, charlie's age is b + 3
    # And jenny's age is b + 8 (since she is 5 years older than charlie and charlie is 3 years older than bobby)

    # We need to find the age of Charlie when Jenny becomes twice as old as Bobby
    # Let's assume x years after this happens
    # Jenny's age would be (b + 8) + x
    # Bobby's age would be b + x
    # And since Jenny is twice as old as Bobby, we have the equation:
    # (b + 8) + x = 2(b + x)

    # Solving for x:
    # b + 8 + x = 2b + 2x
    # x = b + 8

    # So in x years, Jenny will be twice as old as Bobby
    # And since x = b + 8, we have:
    # Charlie's age = (b + 3) + x = (b + 3) + (b + 8) = 2b + 11

    result = 2*b + 11
    return result

print(solution())