def solution():
    """The vending machine fails to drop a snack when it’s purchased one in six times. One in ten times, it will accidentally drop two snacks.
    The rest of the time, it drops the purchased snack. If thirty people have used the vending machine once each to purchase a snack, how many snacks has the vending machine dropped?"""
    # Define the number of people who have used the vending machine
    num_people = 30

    # Define the probability of a failed drop and accidentally dropping two snacks
    fail_prob = 1/6
    double_drop_prob = 1/10

    # Initialize the number of successful drops and accidentally dropped snacks
    success_drops = 0
    double_drops = 0

    # Calculate the number of successful drops and double drops
    for i in range(num_people):
        # Randomly generate a probability between 0 and 1
        prob = random.random()

        if prob < fail_prob: # Failed drop
            pass
        elif prob < fail_prob + double_drop_prob: # Double drop
            double_drops += 2
        else: # Successful drop
            success_drops += 1

    # Calculate the total number of snacks dropped
    total_drops = success_drops + double_drops

    # return the result
    result = total_drops
    return result

print(solution())