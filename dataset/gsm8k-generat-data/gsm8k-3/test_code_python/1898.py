def solution():
    """Walter wants to serve hushpuppies to his guests for his annual fish fry event.  He thinks each guest will eat 5 hushpuppies and he is having 20 guests.  He can cook 10 hushpuppies in 8 minutes.  How long will it take to cook all of the hushpuppies?"""
    # Calculate the total number of hushpuppies needed
    num_hushpuppies = 5 * 20

    # Calculate the number of batches needed to cook all the hushpuppies
    num_batches = num_hushpuppies / 10

    # Calculate the total time needed to cook all the hushpuppies
    time_needed = num_batches * 8

    # Display the time needed to cook all the hushpuppies
    result = time_needed
    return result

print(solution())