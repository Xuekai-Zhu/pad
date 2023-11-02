def solution():
    """The pet shop grooms dogs. It takes 30 minutes to groom a poodle. It takes half as much time to groom a terrier as it takes to groom a poodle. They do not groom cats. If the pet shop grooms 3 poodles and 8 terriers, what is the total length of time it will take, in minutes?"""
    # Define the time it takes to groom a poodle and a terrier
    poodle_time = 30
    terrier_time = poodle_time / 2

    # Calculate the total time to groom the poodles and the terriers
    total_time = (poodle_time * 3) + (terrier_time * 8)

    # Return the result in minutes
    result = total_time
    return result

print(solution())