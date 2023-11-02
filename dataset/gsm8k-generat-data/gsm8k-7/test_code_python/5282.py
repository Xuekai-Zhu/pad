def solution():
    euros = 70
    exchange_rate = 5/1  # 5 euros = 1 dollar
    airport_rate = 5/7  # Willie gets 5/7 of the official exchange rate

    # Convert euros to dollars at the official exchange rate
    dollars_official_rate = euros / exchange_rate

    # Calculate the dollars Willie gets at the airport rate
    dollars_airport_rate = dollars_official_rate * airport_rate

    result = dollars_airport_rate
    return result

print(solution())