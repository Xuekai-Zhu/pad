def solution():
    """The stadium seats 60,000 fans, but only 75% of the seats were sold for the music show. Because of the threat of rain, 5,000 fans stayed home. How many attended the show?"""
    total_seats = 60000
    percent_sold = 75
    num_sold = total_seats * (percent_sold / 100)
    num_attended = num_sold - 5000
    result = num_attended
    return result

print(solution())