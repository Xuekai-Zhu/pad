def solution():
    cookies_start = 0
    cookies_eaten = 3
    cookies_given = 5
    team_members = 8
    cookies_taken = [1, 3, 5, 7, 9, 11, 13, 15]

    # Calculate the total number of cookies given away
    total_given = cookies_eaten + cookies_given

    # Calculate the total number of cookies taken by the basketball team
    total_taken = sum(cookies_taken)

    # Calculate the number of cookies Andy had from the start
    cookies_start = total_given + total_taken

    return cookies_start

print(solution())