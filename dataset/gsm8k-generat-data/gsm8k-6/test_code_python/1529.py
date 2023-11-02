def solution():
    # Calculate the number of females in the town
    females = 5000 - 2000  # 5000 people live in town, 2000 are male

    # Calculate the number of females who wear glasses
    glasses_wearing_females = 0.3 * females

    result = glasses_wearing_females
    return result

print(solution())