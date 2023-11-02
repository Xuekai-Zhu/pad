def solution():
    """Bill decides to bring donuts to work for a meeting that day. He buys a box of donuts that has 50 in total in them. He eats 2 on the ride in because he's hungry. When he gets to the office, the secretary takes another 4 out of the box when he's not looking. Lastly, right before the meeting Bill sets the box down on his desk and leaves the office to take a phone call. While Bill's away, his coworkers steal half the remaining donuts. Bill comes back and brings the box into his meeting. How many donuts are left in the box?"""
    total_donuts = 50
    donuts_eaten = 2
    donuts_stolen = 4
    donuts_left = total_donuts - donuts_eaten - donuts_stolen
    donuts_left /= 2
    result = donuts_left
    return result

print(solution())