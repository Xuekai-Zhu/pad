def solution():
    # Define the cost of the venue and the number of guests John wants
    venue_cost = 10000
    john_guests = 50

    # Calculate the number of guests John's wife wants
    wife_guests = john_guests * 1.6

    # Calculate the cost of the guests
    guest_cost = 500 * (john_guests + wife_guests)

    # Calculate the total cost of the wedding
    total_cost = venue_cost + guest_cost
    result = total_cost
    return result

print(solution())