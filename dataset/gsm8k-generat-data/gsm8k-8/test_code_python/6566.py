def solution():
    # Define the number of guests Thomas initially invites
    initial_guests = 3 * 12

    # Calculate the number of additional guests that will attend
    additional_guests = initial_guests // 3

    # Subtract the number of guests who can't make it from the initial guest count
    final_guests = initial_guests + additional_guests - 5

    # Add 12 extra chairs
    total_chairs = final_guests + 12

    result = total_chairs
    return result

print(solution())