def solution():
    """Chris buys 2 and a half dozen donuts on his way to work to share with his co-workers.  While driving, he eats 10% of the donuts.  Once inside, he grabs another 4 donuts for his afternoon snack.  How many donuts are left for his co-workers?"""
    # Define the number of donuts in a dozen
    DONUTS_PER_DOZEN = 12

    # Define the number of dozens of donuts Chris bought
    dozens_of_donuts = 2.5

    # Calculate the total number of donuts Chris bought
    total_donuts = dozens_of_donuts * DONUTS_PER_DOZEN

    # Calculate the number of donuts Chris ate while driving
    donuts_eaten = total_donuts * 0.1

    # Calculate the number of donuts Chris had left after eating while driving
    donuts_left = total_donuts - donuts_eaten

    # Calculate the number of donuts Chris had left after getting his afternoon snack
    donuts_left -= 4

    # Display the number of donuts Chris had left for his co-workers
    result = donuts_left
    return result

print(solution())