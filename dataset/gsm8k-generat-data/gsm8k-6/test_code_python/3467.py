def solution():
    # Calculate the number of special bills George received
    num_bills = 25 - 15

    # Calculate the number of bills George spent
    spent_bills = num_bills * 0.2

    # Calculate the number of bills George will exchange
    exchange_bills = num_bills - spent_bills

    # Calculate the amount of money George will receive from his parents
    money_received = exchange_bills * 1.5

    result = money_received
    return result

print(solution())