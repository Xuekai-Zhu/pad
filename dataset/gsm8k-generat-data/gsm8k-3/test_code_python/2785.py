def solution():
    """John is budgeting for his marriage. The venue cost $10,000. It cost $500 for each guest, and John wants 50 guests while his wife wants 60% more than that. How much would the wedding cost if John's wife gets her way?"""
    # Define the cost of the venue
    VENUE_COST = 10000

    # Define the cost per guest
    GUEST_COST = 500

    # Define the number of guests John wants
    john_guests = 50

    # Calculate the number of guests John's wife wants
    wife_guests = john_guests * 1.6

    # Calculate the cost of the guests
    john_guest_cost = john_guests * GUEST_COST
    wife_guest_cost = wife_guests * GUEST_COST

    # Calculate the total cost of the wedding
    john_cost = VENUE_COST + john_guest_cost
    wife_cost = VENUE_COST + wife_guest_cost

    # Display the total cost if John's wife gets her way
    result = wife_cost
    return result

print(solution())