def solution():
    """Lassie eats half of her bones on Saturday. On Sunday she received 10 more bones. She now has a total of 35 bones. How many bones did she start with before eating them on Saturday?"""
    bones_on_sunday = 35
    extra_bones = 10
    bones_on_saturday = bones_on_sunday - extra_bones
    bones_at_start = bones_on_saturday * 2
    result = bones_at_start
    return result

print(solution())