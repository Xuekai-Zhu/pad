def solution():
    
    # Define the number of guests and the number of cookies per guest
    num_guests = 100
    cookies_per_guest = 15

    # Calculate the total number of cookies
    total_cookies = num_guests * cookies_per_guest

    # Calculate the number of cookies the bride will give to the church next door
    cookies_given_to_church_next_door = total_cookies / 2

    # Calculate the number of people in the church next door
    num_people = total_cookies / cookies_given_to_church_next_door

    # Display the number of people in the church next door
    result = num_people
    return result

print(solution())