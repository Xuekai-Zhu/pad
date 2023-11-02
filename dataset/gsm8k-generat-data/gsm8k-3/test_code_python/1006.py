def solution():
    """When Jayson is 10 his dad is four times his age and his mom is 2 years younger than his dad.  How old was Jayson's mom when he was born?"""
    # Let x be Jayson's age when he was born
    # Dad's age when Jayson is 10: 4*10=40
    dad_age = 40
    # Mom's age when Jayson is 10: 40-2=38
    mom_age = 38
    # Jayson was born x years ago, so his mom's age at that time was:
    mom_age_at_birth = mom_age - x

    # We need to solve for x
    # We know that when Jayson is 10:
    # dad_age = 4 * Jayson's age
    # So when Jayson was born:
    # dad_age = 4 * (x + 10)
    # Simplifying:
    # 40 = 4x + 40
    # 4x = 0
    # x = 0
    # Therefore Jayson was just born, and his mom's age was:
    mom_age_at_birth = 37

    # Display Jayson's mom's age when he was born
    result = mom_age_at_birth
    return result

print(solution())