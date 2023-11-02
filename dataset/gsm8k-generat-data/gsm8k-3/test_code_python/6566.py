def solution():
    """Thomas wants to throw a party for his best friend Casey. He needs to order enough chairs for all the party guests to sit in, one for each guest. First he orders 3 dozen chairs for 3 dozen guests he invites. Then he finds out that 1/3 of the guests want to bring a guest of their own, so Thomas needs to order more chairs. Eventually, Thomas finds out that 5 of the guests he originally invited can't make it. Thomas would also like to order 12 extra chairs just in case they need them. How many chairs is Thomas going to order for Casey's party?"""
    # Define the number of dozen chairs ordered for the initial guests
    initial_guests = 3
    chairs_per_dozen = 12
    initial_chairs = initial_guests * chairs_per_dozen

    # Define the percentage of guests bringing a plus one
    plus_one_percent = 1/3

    # Calculate the new total number of guests
    new_guests = int(initial_guests * (1 + plus_one_percent))

    # Calculate the number of guests who cancelled
    cancelled_guests = 5

    # Calculate the final number of guests
    final_guests = new_guests - cancelled_guests

    # Define the number of extra chairs ordered
    extra_chairs = 12

    # Calculate the total number of chairs needed
    total_chairs = final_guests + extra_chairs

    # Display the total number of chairs needed
    result = total_chairs
    return result

print(solution())