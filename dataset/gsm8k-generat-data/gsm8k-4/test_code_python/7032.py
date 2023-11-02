def solution():
    """Chris buys 2 and a half dozen donuts on his way to work to share with his co-workers. While driving, he eats 10% of the donuts. Once inside, he grabs another 4 donuts for his afternoon snack. How many donuts are left for his co-workers?"""
    # Define the initial number of donuts
    initial_donuts = 2.5 * 12

    # Calculate the number of donuts Chris ate while driving
    driving_donuts = int(initial_donuts * 0.1)

    # Calculate the number of donuts left after driving
    remaining_donuts = initial_donuts - driving_donuts

    # Calculate the number of donuts Chris grabbed for his afternoon snack
    afternoon_donuts = 4

    # Calculate the final number of donuts
    final_donuts = remaining_donuts - afternoon_donuts

    # Display the number of donuts left for Chris's co-workers
    result = final_donuts
    return result

print(solution())