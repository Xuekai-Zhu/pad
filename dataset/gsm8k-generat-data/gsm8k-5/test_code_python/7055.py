def solution():
    cindy_marbles = 20  # Cindy had 20 marbles
    lisa_marbles = cindy_marbles - 5  # Lisa had 5 less marbles than Cindy

    # After Cindy gives 12 marbles to Lisa
    cindy_marbles -= 12
    lisa_marbles += 12

    # Calculate how many more marbles Lisa has now compared to before
    more_marbles = lisa_marbles - (cindy_marbles + 5)
    result = more_marbles
    return result

print(solution())