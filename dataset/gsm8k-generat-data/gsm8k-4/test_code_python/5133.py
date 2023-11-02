def solution():
    """The local school is holding a big fair to raise money for 5 classes that want to go on a trip. 150 people came to the party and paid a total of $368 for entrance tickets. There was a raffle which brought in $343. The sale of cakes and drinks brought $279. At the end of the fair, the principal of the school shared the money raised between the 5 classes. How much money did each class receive?"""
    # Define the total amount of money raised
    total_money = 368 + 343 + 279

    # Define the number of classes and calculate the amount of money each class should receive
    num_classes = 5
    class_share = total_money / num_classes

    # Return the result
    result = class_share
    return result

print(solution())