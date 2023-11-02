def solution():
    """Bill decides to bring donuts to work for a meeting that day. He buys a box of donuts that has 50 in total in them. He eats 2 on the ride in because he's hungry. When he gets to the office, the secretary takes another 4 out of the box when he's not looking. Lastly, right before the meeting Bill sets the box down on his desk and leaves the office to take a phone call. While Bill's away, his coworkers steal half the remaining donuts. Bill comes back and brings the box into his meeting. How many donuts are left in the box?"""
    total_donuts = 50
    eaten_on_ride = 2
    taken_by_secretary = 4
    remaining_donuts = total_donuts - eaten_on_ride - taken_by_secretary
    remaining_donuts = remaining_donuts / 2
    result = int(remaining_donuts)
    return result

print(solution())