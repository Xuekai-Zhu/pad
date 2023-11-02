def solution():
    """Marcus has received a commission for as many paintings as possible. Marcus plans out his drawings so that his client can receive some of the paintings as soon as possible but it is still going to take a long time. On the first day, he paints 2 paintings. He then paints every day and each day, he paints twice as many paintings as he painted the day before. If he paints for 5 days, how many paintings will he have painted in total?"""
    # Define the number of paintings on the first day
    day1_paintings = 2

    # Initialize the total number of paintings
    total_paintings = day1_paintings

    # Calculate the number of paintings on each of the following days
    current_paintings = day1_paintings
    for i in range(1, 5):
        current_paintings *= 2
        total_paintings += current_paintings

    # Display the total number of paintings
    result = total_paintings
    return result

print(solution())