def solution():
    # Define initial variables
    accidents = 1
    tickets = 3
    base_premium = 50

    # Calculate increase in premium due to accidents
    accident_increase = 0.1 * base_premium * accidents

    # Calculate increase in premium due to tickets
    ticket_increase = 5 * tickets

    # Calculate new premium
    new_premium = base_premium + accident_increase + ticket_increase

    result = new_premium
    return result

print(solution())