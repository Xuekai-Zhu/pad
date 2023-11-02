def solution():
    # Define Elvis' favorite snack ingredients
    peanut_butter = "peanuts"
    bananas = "banana plants"
    # Check if plants were crucial for his snack
    if peanut_butter in "plants" or bananas in "plants":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())