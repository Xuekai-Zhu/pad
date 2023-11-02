def solution():
    """Mrs. Lopez and her family are going to the movie theatre. Adult tickets are $11. Children’s tickets (ages 3-12) are $8. Senior citizen’s tickets (ages 60+) are $9. Mrs. Lopez needs to buy movie tickets for her husband, herself, her parents (ages 72 and 75), and her three children (ages 7, 10, 14). How much money does she need to buy everyone’s tickets?"""
    # Define the ticket prices
    ADULT_TICKET_PRICE = 11
    CHILD_TICKET_PRICE = 8
    SENIOR_TICKET_PRICE = 9

    # Define the ages of Mrs. Lopez's family members
    husband_age = "adult"
    mrs_lopez_age = "adult"
    parent1_age = 75
    parent2_age = 72
    child1_age = 7
    child2_age = 10
    child3_age = 14

    # Determine the cost of each person's ticket based on their age
    if husband_age == "adult":
        husband_ticket_price = ADULT_TICKET_PRICE
    elif husband_age == "child":
        husband_ticket_price = CHILD_TICKET_PRICE
    else:
        husband_ticket_price = SENIOR_TICKET_PRICE

    if mrs_lopez_age == "adult":
        mrs_lopez_ticket_price = ADULT_TICKET_PRICE
    elif mrs_lopez_age == "child":
        mrs_lopez_ticket_price = CHILD_TICKET_PRICE
    else:
        mrs_lopez_ticket_price = SENIOR_TICKET_PRICE

    if parent1_age >= 60:
        parent1_ticket_price = SENIOR_TICKET_PRICE
    elif parent1_age >= 3 and parent1_age <= 12:
        parent1_ticket_price = CHILD_TICKET_PRICE
    else:
        parent1_ticket_price = ADULT_TICKET_PRICE

    if parent2_age >= 60:
        parent2_ticket_price = SENIOR_TICKET_PRICE
    elif parent2_age >= 3 and parent2_age <= 12:
        parent2_ticket_price = CHILD_TICKET_PRICE
    else:
        parent2_ticket_price = ADULT_TICKET_PRICE

    if child1_age >= 3 and child1_age <= 12:
        child1_ticket_price = CHILD_TICKET_PRICE
    elif child1_age >= 60:
        child1_ticket_price = SENIOR_TICKET_PRICE
    else:
        child1_ticket_price = ADULT_TICKET_PRICE

    if child2_age >= 3 and child2_age <= 12:
        child2_ticket_price = CHILD_TICKET_PRICE
    elif child2_age >= 60:
        child2_ticket_price = SENIOR_TICKET_PRICE
    else:
        child2_ticket_price = ADULT_TICKET_PRICE

    if child3_age >= 3 and child3_age <= 12:
        child3_ticket_price = CHILD_TICKET_PRICE
    elif child3_age >= 60:
        child3_ticket_price = SENIOR_TICKET_PRICE
    else:
        child3_ticket_price = ADULT_TICKET_PRICE

    # Calculate the total cost of all the tickets
    total_cost = (husband_ticket_price + mrs_lopez_ticket_price + parent1_ticket_price + parent2_ticket_price + child1_ticket_price + child2_ticket_price + child3_ticket_price)

    # return the result
    result = total_cost
    return result

print(solution())