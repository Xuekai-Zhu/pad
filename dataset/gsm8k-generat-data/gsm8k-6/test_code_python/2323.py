def solution():
    # Calculate the number of people who RSVPed
    rsvped = 200 * 0.9  

    # Calculate the number of people who showed up
    showed_up = rsvped * 0.8  

    # Calculate the number of people who got a gift
    got_gift = showed_up - 10  

    # Calculate the number of thank you cards needed
    cards_needed = got_gift  

    result = cards_needed
    return result

print(solution())