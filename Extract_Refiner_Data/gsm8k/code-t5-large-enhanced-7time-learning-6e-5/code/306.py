def solution():
    
    # Define the cost of each item
    BUSINESS_SUIT_PRICE = 100
    SUITCASE_PRICE = 50
    FLIGHT_TICKET_PRICE = 700

    # Define the number of each item purchased
    num_business_suits = 6
    num_suitcases = 3

    # Calculate the total cost of the business suits
    total_business_suit_cost = num_business_suits * BUSINESS_SUIT_PRICE + num_suitcases * SUITCASE_PRICE

    # Calculate the cost of the flight ticket
    total_flight_ticket_cost = (5 * BUSINESS_SUIT_PRICE) + FLIGHT_TICKET_PRICE

    # Calculate the total cost of the gifts
    total_gift_cost = total_business_suit_cost + total_flight_ticket_cost + 2000

    # Display the total cost of the gifts
    result = total_gift_cost
    return result

print(solution())