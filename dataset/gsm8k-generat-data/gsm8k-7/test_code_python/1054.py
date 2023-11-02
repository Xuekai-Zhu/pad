def solution():
    ticket_price = 50.0
    processing_fee = 0.15  # 15% processing fee
    parking_fee = 10.0
    entrance_fee_per_person = 5.0
    num_people = 2  # Seth and his brother

    # Calculate the total cost of the tickets including the processing fee
    total_ticket_cost = (ticket_price * num_people) * (1 + processing_fee)

    # Calculate the total cost of parking
    total_parking_cost = parking_fee

    # Calculate the total cost of entrance fees
    total_entrance_cost = entrance_fee_per_person * num_people

    # Calculate the total cost of going to the concert
    total_cost = total_ticket_cost + total_parking_cost + total_entrance_cost
    result = total_cost
    return result

print(solution())