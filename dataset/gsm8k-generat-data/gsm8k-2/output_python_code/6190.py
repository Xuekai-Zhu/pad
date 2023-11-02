def solution():
    """The stadium seats 60,000 fans, but only 75% of the seats were sold for the music show. Because of the threat of rain, 5,000 fans stayed home. How many attended the show?"""
    total_seats = 60000
    sold_seats = total_seats * 0.75
    attendance = sold_seats - 5000
    result = attendance
    return result

print(solution())