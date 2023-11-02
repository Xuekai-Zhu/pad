def solution():
    # Calculate the number of seats sold for the music show
    seats_sold = 0.75 * 60000  # 75% of the seats were sold

    # Calculate the number of fans who actually attended the show
    fans_attended = seats_sold - 5000  # 5,000 fans stayed home

    result = fans_attended
    return result

print(solution())