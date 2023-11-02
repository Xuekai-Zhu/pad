def solution():
    """Paul eats a lot when he studies. He loves sandwiches and eats them at the same rate every three days. He eats 2 sandwiches the first day, then doubles that number of sandwiches for the second day. On the third day, he doubles the number of sandwiches he ate on the second day. How many sandwiches would Paul eat if he studied 6 days in a row?"""
    # Define the initial number of sandwiches and the doubling rate
    sandwiches = 2
    doubling_rate = 2

    # Initialize the total number of sandwiches
    total_sandwiches = 0

    # Calculate the number of sandwiches Paul eats each day for 6 days
    for i in range(6):
        total_sandwiches += sandwiches
        if (i+1) % 3 == 0:
            doubling_rate *= 2
            sandwiches = doubling_rate
        else:
            sandwiches = doubling_rate
        
    result = total_sandwiches
    return result

print(solution())