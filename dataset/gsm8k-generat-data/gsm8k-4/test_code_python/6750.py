def solution():
    """A Moroccan restaurant received 3 different shipments of couscous. The first two shipments of 7 and 13 pounds arrived on the same day. The next day's shipment was 45 pounds of couscous. If it takes 5 pounds of couscous to make a dish, how many dishes did the restaurant make?"""
    # Define the total amount of couscous received
    total_couscous = 7 + 13 + 45

    # Calculate the number of dishes that can be made
    num_dishes = total_couscous // 5

    result = num_dishes
    return result

print(solution())