def solution():
    total_price = 23  # total price paid by Elise
    base_price = 3  # base price charged by the cab company
    price_per_mile = 4  # price charged per mile
    miles_travelled = (total_price - base_price) / price_per_mile  # calculate the distance travelled
    result = miles_travelled
    return result

print(solution())