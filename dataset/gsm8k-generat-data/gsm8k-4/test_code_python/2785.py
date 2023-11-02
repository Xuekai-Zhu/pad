def solution():
    """John is budgeting for his marriage. The venue cost $10,000. It cost $500 for each guest, and John wants 50 guests while his wife wants 60% more than that. How much would the wedding cost if John's wife gets her way?"""
    # Define the initial cost of the wedding venue
    venue_cost = 10000

    # Define the cost per guest
    guest_cost = 500

    # Define the number of guests John wants
    john_guests = 50

    # Calculate the number of guests John's wife wants
    wife_guests = john_guests * 1.6

    # Calculate the total cost of the wedding
    total_cost = venue_cost + (john_guests * guest_cost) + (wife_guests * guest_cost)

    result = total_cost
    return result

print(solution())