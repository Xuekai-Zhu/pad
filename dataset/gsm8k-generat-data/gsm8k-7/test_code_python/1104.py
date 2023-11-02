def solution():
    total_tickets_sold = 900

    # Calculate the number of people who came before the start of the concert
    num_came_before = total_tickets_sold * (3/4)

    # Calculate the remaining number of people who haven't come before the start of the concert
    num_remaining = total_tickets_sold - num_came_before

    # Calculate the number of people who came few minutes after the first song
    num_came_after_song = num_remaining * (5/9)

    # Calculate the remaining number of people who haven't come yet
    num_remaining = num_remaining - num_came_after_song - 80

    # Calculate the number of people who did not go
    num_did_not_go = num_remaining

    result = num_did_not_go
    return result

print(solution())