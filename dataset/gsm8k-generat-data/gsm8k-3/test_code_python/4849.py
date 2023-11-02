def solution():
    """The pet shop grooms dogs.  It takes 30 minutes to groom a poodle.  It takes half as much time to groom a terrier as it takes to groom a poodle.  They do not groom cats.  If the pet shop grooms 3 poodles and 8 terriers, what is the total length of time it will take, in minutes?"""
    # Define the grooming time for a poodle
    POODLE_TIME = 30

    # Define the grooming time for a terrier as half the grooming time for a poodle
    TERRIER_TIME = POODLE_TIME / 2

    # Calculate the total time to groom the poodles
    poodle_time = POODLE_TIME * 3

    # Calculate the total time to groom the terriers
    terrier_time = TERRIER_TIME * 8

    # Calculate the total grooming time
    total_time = poodle_time + terrier_time

    # Display the total grooming time
    result = total_time
    return result

print(solution())