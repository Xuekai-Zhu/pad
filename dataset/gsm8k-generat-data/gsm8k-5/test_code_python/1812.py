def solution():
    total_time = 9  # Bret takes a 9 hour train ride to go to Boston
    time_spent_reading = 2  # Bret spends 2 hours reading a book
    time_spent_eating = 1  # Bret spends 1 hour to eat his dinner
    time_spent_watching = 3  # Bret spends 3 hours watching movies on his computer

    # Calculate the total time Bret spent not napping
    total_time_spent = time_spent_reading + time_spent_eating + time_spent_watching

    # Calculate the time Bret has left to take a nap
    time_left_to_nap = total_time - total_time_spent
    result = time_left_to_nap
    return result

print(solution())