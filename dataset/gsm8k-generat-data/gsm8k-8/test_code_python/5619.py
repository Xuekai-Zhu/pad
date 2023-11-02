def solution():
    # Define the value of each bill and coin
    hundred_bill = 100
    fifty_bill = 50
    twenty_bill = 20
    ten_bill = 10
    five_bill = 5
    one_coin = 1

    # Add up the total value of bills and coins in the till
    total_value = 2*hundred_bill + 1*fifty_bill + 5*twenty_bill + 3*ten_bill + 7*five_bill + 27*one_coin

    # Subtract $300 from the total value to find the amount to turn in
    amount_to_turn_in = total_value - 300
    result = amount_to_turn_in
    return result

print(solution())