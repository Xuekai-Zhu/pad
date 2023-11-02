def solution():
    """Marcus has received a commission for as many paintings as possible. Marcus plans out his drawings so that his client can receive some of the paintings as soon as possible but it is still going to take a long time. On the first day, he paints 2 paintings. He then paints every day and each day, he paints twice as many paintings as he painted the day before. If he paints for 5 days, how many paintings will he have painted in total?"""
    # Initialize the total number of paintings and the number of paintings painted on the first day
    total_paintings = 2
    paintings_on_first_day = 2

    # Loop through each day that Marcus painted
    for day in range(2, 6):
        # Calculate the number of paintings painted on this day
        paintings_on_this_day = paintings_on_first_day * (2 ** (day - 2))

        # Add the number of paintings to the total
        total_paintings += paintings_on_this_day

    # return the result
    result = total_paintings
    return result

print(solution())