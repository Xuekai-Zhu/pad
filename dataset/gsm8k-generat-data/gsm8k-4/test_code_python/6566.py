def solution():
    """Thomas wants to throw a party for his best friend Casey. He needs to order enough chairs for all the party guests to sit in, one for each guest. First he orders 3 dozen chairs for 3 dozen guests he invites. Then he finds out that 1/3 of the guests want to bring a guest of their own, so Thomas needs to order more chairs. Eventually, Thomas finds out that 5 of the guests he originally invited can't make it. Thomas would also like to order 12 extra chairs just in case they need them. How many chairs is Thomas going to order for Casey's party?"""
    # Define the initial number of guests and chairs
    initial_guests = 36
    initial_chairs = 36

    # Calculate the number of additional guests and chairs needed
    additional_guests = initial_guests * (1/3)
    additional_chairs = round(additional_guests)

    # Subtract the number of guests who can't make it
    final_guests = initial_guests + additional_guests - 5
    final_chairs = initial_chairs + additional_chairs + 12

    # Return the final number of chairs needed
    result = final_chairs
    return result

print(solution())