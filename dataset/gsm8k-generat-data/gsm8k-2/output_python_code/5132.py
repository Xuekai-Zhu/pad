def solution():
    """The local school is holding a big fair to raise money for 5 classes that want to go on a trip. 150 people came to the party and paid a total of $368 for entrance tickets. There was a raffle which brought in $343. The sale of cakes and drinks brought $279. At the end of the fair, the principal of the school shared the money raised between the 5 classes. How much money did each class receive?"""
    total_money_raised = 368 + 343 + 279
    num_classes = 5
    money_each_class = total_money_raised / num_classes
    result = money_each_class
    return result

print(solution())