def solution():
    # Jeff starts with 20 cats
    current_cats = 20

    # Add the 2 kittens he found on Monday
    current_cats += 2

    # Add the injured cat he found on Tuesday
    current_cats += 1

    # Subtract the 6 cats that were adopted on Wednesday
    current_cats -= 6

    result = current_cats
    return result

print(solution())