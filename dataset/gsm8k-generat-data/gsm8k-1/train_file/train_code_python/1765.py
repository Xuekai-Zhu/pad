def solution():
    """Ephraim has two machines that make necklaces for his store. On Sunday the first machine made 45 necklaces. The second machine made 2.4 times as many necklaces as the first machine. How many necklaces were made in total on Sunday?"""
    machine1_necklaces = 45
    machine2_necklaces = machine1_necklaces * 2.4
    total_necklaces = machine1_necklaces + machine2_necklaces
    result = total_necklaces
    return result

print(solution())