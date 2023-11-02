def solution():
    """Aiden and 12 of his friends are going to see a film at the cinema, and meet up with 7 more friends there. They each save a seat and then buy enough drinks and snacks to fill the seats. Each seat has enough room to hold one person, two drinks, and three snacks. If drinks and snacks cost $2 each, how much money, in dollars, has the group spent overall on snacks and drinks?"""
    num_friends = 12 + 7
    num_seats = num_friends
    num_drinks_per_seat = 2
    num_snacks_per_seat = 3
    cost_per_item = 2
    num_drinks = num_seats * num_drinks_per_seat
    num_snacks = num_seats * num_snacks_per_seat
    total_cost = (num_drinks + num_snacks) * cost_per_item
    result = total_cost
    return result

print(solution())