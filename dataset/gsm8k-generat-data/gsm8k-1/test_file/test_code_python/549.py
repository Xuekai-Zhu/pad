def solution():
    """Bill is trying to figure out how many water bottles he needs to buy for his party. He started out with 2 cases of water which have 24 bottles each. He has 70 guests that will be arriving, and he wants to have 2 bottles of water for each guest. How many additional bottles of water will he need to buy?"""
    initial_bottles = 2 * 24  # 2 cases with 24 bottles each
    guests = 70
    bottles_per_guest = 2
    total_bottles = initial_bottles + (guests * bottles_per_guest)
    additional_bottles = total_bottles - (2 * 24)  # Subtract the initial bottles
    result = additional_bottles
    return result

print(solution())