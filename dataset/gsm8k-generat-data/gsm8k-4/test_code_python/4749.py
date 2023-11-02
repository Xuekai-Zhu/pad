def solution():
    """Lassie eats half of her bones on Saturday. On Sunday she received 10 more bones. She now has a total of 35 bones. How many bones did she start with before eating them on Saturday?"""
    # Define the number of bones Lassie had before eating them on Saturday
    bones_saturday = None

    # Define the number of bones Lassie received on Sunday
    bones_sunday = 10

    # Calculate the total number of bones Lassie has now
    bones_total = 35

    # Calculate the number of bones Lassie had before eating them on Saturday
    bones_saturday = (bones_total - bones_sunday) * 2

    result = bones_saturday
    return result

print(solution())