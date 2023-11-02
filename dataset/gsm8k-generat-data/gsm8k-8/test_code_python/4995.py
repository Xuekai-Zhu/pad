def solution():
    # Calculate the total number of songs John buys in a month
    total_songs = 20 * 60 / 3

    # Calculate the monthly cost of the songs
    monthly_cost = total_songs * 0.50

    # Calculate the yearly cost of the songs
    yearly_cost = monthly_cost * 12

    result = yearly_cost
    return result

print(solution())