def solution():
    school_size = 400  # The school has 400 people
    half_school = school_size / 2  # Half of the school attended the party
    collected_amount = 2000  # The party collected $2000 with half the school attending

    # Calculate the amount collected if 300 people attended the party
    amount_300_people = collected_amount * (300 / half_school)
    result = amount_300_people
    return result

print(solution())