def solution():
    """Walter wants to serve hushpuppies to his guests for his annual fish fry event. He thinks each guest will eat 5 hushpuppies and he is having 20 guests. He can cook 10 hushpuppies in 8 minutes. How long will it take to cook all of the hushpuppies?"""
    guests = 20
    hushpuppies_per_guest = 5
    total_hushpuppies = guests * hushpuppies_per_guest
    hushpuppies_per_batch = 10
    time_per_batch = 8
    batches_needed = total_hushpuppies // hushpuppies_per_batch + \
        (1 if total_hushpuppies % hushpuppies_per_batch != 0 else 0)
    total_time = batches_needed * time_per_batch
    result = total_time
    return result

print(solution())