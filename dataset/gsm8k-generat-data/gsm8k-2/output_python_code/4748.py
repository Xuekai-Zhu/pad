def solution():
    """Lassie eats half of her bones on Saturday. On Sunday she received 10 more bones. She now has a total of 35 bones. How many bones did she start with before eating them on Saturday?"""
    total_bones = 35
    bones_on_sunday = total_bones - (total_bones * 0.5) - 10
    bones_on_saturday = bones_on_sunday * 2
    total_bones_start = bones_on_saturday + bones_on_sunday
    result = total_bones_start
    return result

print(solution())