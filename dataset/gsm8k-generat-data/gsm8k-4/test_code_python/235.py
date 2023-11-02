def solution():
    """Max likes to collect model trains. He asks for one for every birthday of his, and asks for two each Christmas. Max always gets the gifts he asks for, and asks for these same gifts every year for 5 years. At the end of the 5 years, his parents give him double the number of trains he already has. How many trains does Max have now?"""
    # Define the number of trains received each year
    birthday_trains = 1
    christmas_trains = 2

    # Initialize the total number of trains
    total_trains = 0

    # Calculate the number of trains received over 5 years
    for i in range(5):
        total_trains += birthday_trains
        total_trains += christmas_trains

    # Double the number of trains Max already has and add it to the total
    total_trains += total_trains * 2

    result = total_trains
    return result

print(solution())