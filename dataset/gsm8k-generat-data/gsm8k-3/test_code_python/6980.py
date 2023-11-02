def solution():
    """Bill decides to bring donuts to work for a meeting that day.  He buys a box of donuts that has 50 in total in them.  He eats 2 on the ride in because he's hungry.  When he gets to the office, the secretary takes another 4 out of the box when he's not looking.  Lastly, right before the meeting Bill sets the box down on his desk and leaves the office to take a phone call.  While Bill's away, his coworkers steal half the remaining donuts.  Bill comes back and brings the box into his meeting.  How many donuts are left in the box?"""
    # Define the starting number of donuts
    starting_donuts = 50

    # Subtract the donuts that Bill ate on the ride in
    remaining_donuts = starting_donuts - 2

    # Subtract the donuts that the secretary took
    remaining_donuts -= 4

    # Subtract the donuts that Bill's coworkers stole while he was away
    remaining_donuts //= 2

    # Display the number of donuts remaining in the box
    result = remaining_donuts
    return result

print(solution())