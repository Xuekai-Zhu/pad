def solution():
    hare_height = 14  # The hare is 14 inches tall
    camel_height = 24 * hare_height  # The camel is 24 times taller than the hare

    # Convert the camel's height from inches to feet
    camel_height_in_feet = camel_height / 12
    result = camel_height_in_feet
    return result

print(solution())