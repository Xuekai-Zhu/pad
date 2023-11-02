def solution():
    """The local school is holding a big fair to raise money for 5 classes that want to go on a trip. 150 people came to the party and paid a total of $368 for entrance tickets. There was a raffle which brought in $343. The sale of cakes and drinks brought $279. At the end of the fair, the principal of the school shared the money raised between the 5 classes. How much money did each class receive?"""
    # Define the total money raised
    total_money = 368 + 343 + 279

    # Divide the total money raised by the number of classes to get the amount each class receives
    class_share = total_money / 5

    # Display the amount each class receives
    result = class_share
    return result

print(solution())