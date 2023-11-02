def solution():
    days_to_take_vitamins = 180  # Barry needs to take vitamin D3 for 180 days
    capsules_per_bottle = 60  # Each bottle contains 60 capsules
    servings_per_day = 2  # Barry needs to take 2 capsules per day

    # Calculate the total number of capsules Barry needs for 180 days
    total_capsules = days_to_take_vitamins * servings_per_day

    # Calculate the total number of bottles Barry needs to buy
    total_bottles = total_capsules // capsules_per_bottle + (total_capsules % capsules_per_bottle > 0)

    result = total_bottles
    return result

print(solution())