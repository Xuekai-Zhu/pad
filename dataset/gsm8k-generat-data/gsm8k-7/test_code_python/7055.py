def solution():
    cindy_marbles = 20
    lisa_marbles = cindy_marbles - 5
    cindy_gave = 12

    # Calculate how many marbles Cindy has now
    cindy_marbles -= cindy_gave

    # Calculate how many marbles Lisa has now
    lisa_marbles += cindy_gave

    # Calculate the difference in marbles Lisa has now compared to before
    difference = lisa_marbles - (cindy_marbles - 5)
    result = difference
    return result

print(solution())