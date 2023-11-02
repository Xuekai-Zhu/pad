def solution():
    """Walter wants to serve hushpuppies to his guests for his annual fish fry event. He thinks each guest will eat 5 hushpuppies and he is having 20 guests. He can cook 10 hushpuppies in 8 minutes. How long will it take to cook all of the hushpuppies?"""
    # Define the number of guests and hushpuppies per guest
    guests = 20
    hushpuppies_per_guest = 5

    # Calculate the total number of hushpuppies needed
    total_hushpuppies = guests * hushpuppies_per_guest

    # Define the cooking rate
    cooking_rate = 10 / 8  # hushpuppies per minute

    # Calculate the time to cook all the hushpuppies
    cooking_time = total_hushpuppies / cooking_rate  # minutes

    result = cooking_time
    return result

print(solution())