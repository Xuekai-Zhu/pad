def solution():
    """Thomas wants to throw a party for his best friend Casey. He needs to order enough chairs for all the party guests to sit in, one for each guest. First he orders 3 dozen chairs for 3 dozen guests he invites. Then he finds out that 1/3 of the guests want to bring a guest of their own, so Thomas needs to order more chairs. Eventually, Thomas finds out that 5 of the guests he originally invited can't make it. Thomas would also like to order 12 extra chairs just in case they need them. How many chairs is Thomas going to order for Casey's party?"""
    initial_guests = 3 * 12
    additional_guests = initial_guests * (1/3)
    total_guests = initial_guests + additional_guests - 5
    total_chairs = total_guests + 12
    result = total_chairs
    return result

print(solution())