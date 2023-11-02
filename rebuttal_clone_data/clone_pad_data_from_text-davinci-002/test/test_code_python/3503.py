def solution():
    total_seats = 60000
    percent_sold = 75
    seats_sold = total_seats * (percent_sold / 100)
    fans_that_came = seats_sold - 5000
    result = fans_that_came
    return result

print(solution())