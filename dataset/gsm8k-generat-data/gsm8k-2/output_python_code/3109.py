def solution():
    """Mrs. Lopez and her family are going to the movie theatre. Adult tickets are $11. Children’s tickets (ages 3-12)
    are $8. Senior citizen’s tickets (ages 60+) are $9. Mrs. Lopez needs to buy movie tickets for her husband,
    herself, her parents (ages 72 and 75), and her three children (ages 7, 10, 14). How much money does she need
    to buy everyone’s tickets?"""
    adult_ticket_price = 11
    child_ticket_price = 8
    senior_ticket_price = 9
    num_adults = 2
    num_children = 3
    num_seniors = 2
    adult_total_price = num_adults * adult_ticket_price
    child_total_price = num_children * child_ticket_price
    senior_total_price = num_seniors * senior_ticket_price
    total_price = adult_total_price + child_total_price + senior_total_price
    result = total_price
    return result

print(solution())