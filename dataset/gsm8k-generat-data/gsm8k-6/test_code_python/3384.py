def solution():
    # Calculate the number of capsules Barry needs to last for 180 days
    total_capsules = 180 * 2  # Barry needs to take 2 capsules every day for 180 days

    # Calculate the number of bottles Barry needs to buy
    bottles_needed = total_capsules / 60  # each bottle contains 60 capsules

    # Round up to the nearest whole number
    bottles_needed = math.ceil(bottles_needed)

    result = bottles_needed
    return result

print(solution())