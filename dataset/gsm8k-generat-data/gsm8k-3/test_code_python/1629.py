def solution():
    """The zoo has 50 new visitors entering the zoo every hour. The zoo is open for 8 hours in one day. If 80% of the total visitors go to the gorilla exhibit, how many visitors go to the gorilla exhibit in one day?"""
    # Define the number of new visitors per hour and the number of hours the zoo is open
    NEW_VISITORS_PER_HOUR = 50
    HOURS_OPEN = 8

    # Calculate the total number of visitors in one day
    total_visitors = NEW_VISITORS_PER_HOUR * HOURS_OPEN

    # Calculate the number of visitors that go to the gorilla exhibit
    gorilla_visitors = total_visitors * 0.8

    # Display the number of visitors that go to the gorilla exhibit
    result = gorilla_visitors
    return result

print(solution())