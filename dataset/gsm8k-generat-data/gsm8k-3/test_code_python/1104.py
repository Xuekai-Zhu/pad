def solution():
    """Nine hundred tickets were sold to a concert. Three-fourths of those who bought the ticket came before the start of the concert. Five-ninths of the remaining came few minutes after the first song. Eighty people arrived during the middle part of the concert while the rest did not go. How many of those who bought the tickets did not go?"""
    # Define the total number of tickets sold
    total_tickets = 900

    # Calculate the number of people who came before the start of the concert
    before_concert = int(total_tickets * (3/4))

    # Calculate the remaining number of tickets
    remaining_tickets = total_tickets - before_concert

    # Calculate the number of people who came after the first song
    after_first_song = int(remaining_tickets * (5/9))

    # Calculate the number of people who did not go to the concert
    not_going = total_tickets - before_concert - after_first_song - 80

    # Display the number of people who did not go to the concert
    result = not_going
    return result

print(solution())