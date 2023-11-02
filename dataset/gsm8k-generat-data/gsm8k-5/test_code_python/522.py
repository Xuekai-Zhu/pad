def solution():
    hoots_per_minute = 20 - 5  # 5 less than 20 hoots per minute are heard
    hoots_per_owl = 5  # One barnyard owl makes 5 hoot sounds per minute

    # Calculate the number of owls making the heard hoots per minute
    owls = hoots_per_minute / hoots_per_owl
    result = owls
    return result

print(solution())