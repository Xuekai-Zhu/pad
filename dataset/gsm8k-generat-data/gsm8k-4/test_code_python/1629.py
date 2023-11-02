def solution():
    """The zoo has 50 new visitors entering the zoo every hour. The zoo is open for 8 hours in one day. If 80% of the total visitors go to the gorilla exhibit, how many visitors go to the gorilla exhibit in one day?"""
    # Define the number of new visitors per hour and the number of hours the zoo is open
    visitors_per_hour = 50
    hours_open = 8

    # Calculate the total number of visitors
    total_visitors = visitors_per_hour * hours_open

    # Calculate the number of visitors who go to the gorilla exhibit
    gorilla_visitors = total_visitors * 0.8

    # Return the result
    result = gorilla_visitors
    return result

print(solution())