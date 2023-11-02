def solution():
    # Calculate the amount of dollars Willie gets at the airport
    exchange_rate = 5/1  # 5 euros is worth 1 dollar
    airport_rate = exchange_rate * (5/7)  # the airport exchange rate is 5/7ths of the official exchange rate
    dollars = 70 * airport_rate  # Willie had 70 euros
    result = dollars
    return result

print(solution())