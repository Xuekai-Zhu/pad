def solution():
    """Ephraim has two machines that make necklaces for his store. On Sunday the first machine made 45 necklaces. The second machine made 2.4 times as many necklaces as the first machine. How many necklaces were made in total on Sunday?"""
    # Define the number of necklaces made by the first machine
    machine_1_necklaces = 45

    # Calculate the number of necklaces made by the second machine
    machine_2_necklaces = machine_1_necklaces * 2.4

    # Calculate the total number of necklaces made on Sunday
    total_necklaces = machine_1_necklaces + machine_2_necklaces

    result = total_necklaces
    return result

print(solution())