def solution():
    """Bridgette and Alex are getting married. Bridgette is inviting 84 guests, and Alex is inviting two thirds of that number of guests. They hired a caterer to make a plated meal for each guest at the wedding reception. The caterer always makes ten extra plates just in case something goes wrong. Each plate of steak and asparagus in garlic butter will have 8 asparagus spears on it. How many asparagus spears will the caterer need in all?"""
    # Define the number of guests Bridgette is inviting
    bridgette_guests = 84

    # Define the number of guests Alex is inviting
    alex_guests = bridgette_guests * 2 / 3

    # Define the total number of guests
    total_guests = bridgette_guests + alex_guests

    # Define the number of plates needed, including extras
    plates_needed = total_guests + 10

    # Define the number of asparagus spears needed
    asparagus_spears_needed = plates_needed * 8

    # return the result
    result = asparagus_spears_needed
    return result

print(solution())