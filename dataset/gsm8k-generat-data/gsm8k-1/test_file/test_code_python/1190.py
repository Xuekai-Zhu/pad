def solution():
    """From her science class study, Brady learned that each whale in the sea has 40 gallons of blood. She also learned that a shark has three times as much blood as a whale. Calculate the number of gallons of blood that ten sharks swimming in the sea have."""
    whale_blood = 40
    shark_blood = 3 * whale_blood
    num_sharks = 10
    total_shark_blood = shark_blood * num_sharks
    result = total_shark_blood
    return result

print(solution())