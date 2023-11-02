def solution():
    
    # Define the number of guests and cookies per guest
    num_guests = 100
    cookies_per_guest = 15

    # Calculate the total number of cookies
    total_cookies = num_guests * cookies_per_guest

    # Calculate the number of cookies the bride gave to the church next door
    cookies_to_church_next_door = total_cookies / 2

    # Calculate the number of people in the church next door
    num_people_next_door = cookies_to_church_next_door / 15

    # Display the number of people in the church next door
    result = num_people_next_door
    return result

print(solution())