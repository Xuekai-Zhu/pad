def solution():
    # Define the start of fall in New York and the location of Auburn, New York
    ny_fall_start = "September"
    auburn_location = "New York"
    # Check if Auburn, New York falls within the same month as the start of fall in New York
    if ny_fall_start == "September" and auburn_location == "New York":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())