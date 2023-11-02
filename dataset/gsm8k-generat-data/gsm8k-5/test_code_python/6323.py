def solution():
    initial_jellybeans = 90  # The jar initially had 90 jellybeans
    samantha_taken = 24  # Samantha took 24 jellybeans out of the jar
    shelby_eaten = 12  # Shelby ate 12 jellybeans from the jar

    # Calculate how many jellybeans Shannon refilled the jar with
    refill_amount = (samantha_taken + shelby_eaten) / 2

    # Calculate how many jellybeans are in the jar now
    total_jellybeans = initial_jellybeans - samantha_taken - shelby_eaten + refill_amount
    result = total_jellybeans
    return result

print(solution())