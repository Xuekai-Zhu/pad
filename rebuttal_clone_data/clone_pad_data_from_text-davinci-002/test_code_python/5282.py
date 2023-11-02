def solution():
     euros = 70
     official_exchange_rate = 5
     airport_exchange_rate = 5/7
     dollars = euros * (official_exchange_rate / airport_exchange_rate)
     result = dollars
     return result

print(solution())