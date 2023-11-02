def solution():
    """Jeremie wants to go to an amusement park with 3 friends at the end of summer. Tickets are $18 for children and a set of snack cost $5. How much will it cost Jeremie and her 3 friends to go to the amusement park and buy each of them a set of snacks?"""
    num_people = 4
    ticket_price = 18
    snack_price = 5
    total_cost = (num_people * ticket_price) + (num_people * snack_price)
    result = total_cost
    return result

print(solution())