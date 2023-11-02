def solution():
    """The pet shop grooms dogs. It takes 30 minutes to groom a poodle. It takes half as much time to groom a terrier as it takes to groom a poodle. They do not groom cats. If the pet shop grooms 3 poodles and 8 terriers, what is the total length of time it will take, in minutes?"""
    poodle_groom_time = 30
    terrier_groom_time = poodle_groom_time / 2
    total_time = (poodle_groom_time * 3) + (terrier_groom_time * 8)
    result = total_time
    return result

print(solution())