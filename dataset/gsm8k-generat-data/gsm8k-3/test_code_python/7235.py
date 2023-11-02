def solution():
    """Jenny is older than Charlie by five years, while Charlie is older than Bobby by three years. How old will Charlie be when Jenny becomes twice as old as Bobby?"""
    # Let's assume Bobby's current age is x
    # Then Charlie's current age is x + 3
    # And Jenny's current age is x + 8 (since she is older than Charlie by 5 years)
    # We want to find out how old Charlie will be when Jenny becomes twice as old as Bobby
    # Let's call that time "t"

    # At time t, Jenny's age will be (x + 8 + t)
    # And Bobby's age will be (x + t)
    # So we can set up the equation:

    # 2(x + t) = (x + 8 + t)

    # Solving for t:

    # 2x + 2t = x + 8 + t
    # t = 8 - x
    # So in t years, Charlie will be (x + 3 + t) years old

    # Let's assume Bobby is currently 10 years old
    x = 10
    t = 8 - x
    charlie_age_at_t = x + 3 + t

    result = charlie_age_at_t
    return result

print(solution())