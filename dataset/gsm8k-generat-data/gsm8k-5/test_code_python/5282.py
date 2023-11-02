def solution():
    euros = 70  # Willie has 70 euros
    euro_to_dollar_rate = 5  # 5 euros is worth 1 dollar
    exchange_rate = euro_to_dollar_rate * (5/7)  # Exchange rate at the airport is 5/7ths of the official rate
    dollars = euros * exchange_rate  # Convert euros to dollars using the airport exchange rate
    result = dollars
    return result

print(solution())