def solution():
    # Identify the first name of the Redenbacher popcorn founder and Shaggy
    redenbacher_first_name = "Orville"
    shaggy_first_name = "Orville"
    # Check if both individuals would raise their hand during a first name roll call
    if redenbacher_first_name == shaggy_first_name:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())