def solution():
    """Bill decides to bring donuts to work for a meeting that day. He buys a box of donuts that has 50 in total in them. He eats 2 on the ride in because he's hungry. When he gets to the office, the secretary takes another 4 out of the box when he's not looking. Lastly, right before the meeting Bill sets the box down on his desk and leaves the office to take a phone call. While Bill's away, his coworkers steal half the remaining donuts. Bill comes back and brings the box into his meeting. How many donuts are left in the box?"""
    # Define the initial number of donuts
    initial_donuts = 50

    # Define the number of donuts eaten by Bill
    bill_donuts_eaten = 2

    # Define the number of donuts taken by the secretary
    secretary_donuts_taken = 4
    
    #Calculate the number of donuts left after Bill and the secretary had eaten
    donuts_remaining = initial_donuts - bill_donuts_eaten - secretary_donuts_taken
    
    #Calculate the number of remaining donuts after coworkers take half of the remaining donuts
    remaining_donuts_after_coworkers = donuts_remaining / 2
    
    #Calculate the final number of donuts left for the meeting
    final_donuts = remaining_donuts_after_coworkers
    
    #Return the result
    return final_donuts

print(solution())