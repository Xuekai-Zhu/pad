def solution():
    """When Jayson is 10 his dad is four times his age and his mom is 2 years younger than his dad. How old was Jayson's mom when he was born?"""
    # Let x be the age of Jayson's dad when Jayson is 10
    x = 4*10

    # Let y be the age of Jayson's mom when Jayson is 10
    y = x-2

    # Let z be the age of Jayson's mom when Jayson was born (10 years ago)
    z = y-10

    result = z
    return result

print(solution())