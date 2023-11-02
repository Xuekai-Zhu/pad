def solution():
    # Calculate the probability of the vending machine failing to drop a snack and accidentally dropping two snacks
    fail_probability = 1/6
    double_drop_probability = 1/10

    # Calculate the probability of the vending machine dropping one snack
    one_drop_probability = 1 - fail_probability - double_drop_probability

    # Calculate the expected number of snacks dropped for each person
    expected_drops_per_person = 0 * fail_probability + 2 * double_drop_probability + 1 * one_drop_probability

    # Calculate the total number of snacks dropped for all thirty people
    total_drops = expected_drops_per_person * 30
    result = total_drops
    return result

print(solution())