def solution():
    """Nine hundred tickets were sold to a concert. Three-fourths of those who bought the ticket came before the start of the concert. Five-ninths of the remaining came few minutes after the first song. Eighty people arrived during the middle part of the concert while the rest did not go. How many of those who bought the tickets did not go?"""
    # Define the initial number of ticket buyers
    ticket_buyers = 900

    # Calculate the number of ticket buyers who came before the start of the concert
    before_concert = ticket_buyers * (3/4)

    # Calculate the remaining number of ticket buyers
    remaining_buyers = ticket_buyers - before_concert

    # Calculate the number of ticket buyers who came after the first song
    after_first_song = remaining_buyers * (5/9)

    # Calculate the number of ticket buyers who did not go
    did_not_go = ticket_buyers - before_concert - after_first_song - 80

    # return the result
    result = did_not_go
    return result

print(solution())