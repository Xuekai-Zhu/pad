def solution():
    """The vending machine fails to drop a snack when it’s purchased one in six times. One in ten times, it will accidentally drop two snacks. The rest of the time, it drops the purchased snack. If thirty people have used the vending machine once each to purchase a snack, how many snacks has the vending machine dropped?"""
    # Define the probability of the vending machine failing to drop a snack and dropping two snacks
    fail_prob = 1/6
    double_prob = 1/10

    # Calculate the expected number of snacks dropped per person
    expected_dropped = fail_prob + 2 * double_prob

    # Calculate the total expected number of snacks dropped
    total_dropped = 30 * expected_dropped

    # Display the total expected number of snacks dropped
    result = total_dropped
    return result

print(solution())