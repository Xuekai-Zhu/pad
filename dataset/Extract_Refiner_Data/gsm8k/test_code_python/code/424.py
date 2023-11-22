def solution():
    
    # Define the number of guests and the number of guests who were prepared for one hotdog
    guests = 36
    hotdogs_per_guest = 1

    # Calculate the number of guests who were prepared for half of them
    half_guests = guests / 2

    # Calculate the number of guests who wanted a second hotdog
    second_hotdogs = guests - half_guests

    # Display the number of guests who did not get a second hotdog
    result = second_hotdogs
    return result

print(solution())