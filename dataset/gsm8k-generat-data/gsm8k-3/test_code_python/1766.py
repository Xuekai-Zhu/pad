def solution():
    """Ephraim has two machines that make necklaces for his store. On Sunday the first machine made 45 necklaces. The second machine made 2.4 times as many necklaces as the first machine. How many necklaces were made in total on Sunday?"""
    # Define the number of necklaces made by the first machine
    machine1 = 45

    # Define the ratio of necklaces made by the second machine compared to the first
    ratio = 2.4

    # Calculate the number of necklaces made by the second machine
    machine2 = machine1 * ratio

    # Calculate the total number of necklaces made
    total = machine1 + machine2

    # Display the total number of necklaces made
    result = total
    return result

print(solution())