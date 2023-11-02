def solution():
    """The local school is holding a big fair to raise money for 5 classes that want to go on a trip. 150 people came to the party and paid a total of $368 for entrance tickets. There was a raffle which brought in $343. The sale of cakes and drinks brought $279. At the end of the fair, the principal of the school shared the money raised between the 5 classes. How much money did each class receive?"""
    entrance_ticket_revenue = 368
    raffle_revenue = 343
    food_and_drink_revenue = 279
    total_revenue = entrance_ticket_revenue + raffle_revenue + food_and_drink_revenue
    classes = 5
    revenue_per_class = total_revenue / classes
    result = revenue_per_class
    return result

print(solution())