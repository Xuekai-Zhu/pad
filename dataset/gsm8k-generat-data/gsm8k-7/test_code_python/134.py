def solution():
    adult_ticket_price = 109
    child_discount = 5
    num_children = 2
    child_1_age = 6
    child_2_age = 10
    amount_paid = 500

    # Calculate the total amount due for the adult tickets
    adult_total = adult_ticket_price * 2

    # Calculate the total discount for the children's tickets
    child_discount_total = child_discount * num_children

    # Calculate the total amount due for the children's tickets
    child_total = (adult_ticket_price - child_discount) * num_children

    # Calculate the total amount due for all tickets
    total_due = adult_total + child_total

    # Calculate the change due
    change_due = amount_paid - total_due

    result = change_due
    return result

print(solution())