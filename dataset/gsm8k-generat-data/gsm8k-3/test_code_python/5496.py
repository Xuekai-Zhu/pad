def solution():
    """A trolley driver picked up 10 people on his 1st stop.  On the next stop, 3 people got off and twice as many people from the 1st stop got on.  On the third stop, 18 people got off and 2 got on.  How many people are currently on the trolley?"""
    # Define the initial number of people on the trolley
    current_count = 10

    # Calculate the number of people at the second stop
    current_count -= 3 # three people got off
    current_count += 2*10 # twice as many people from the first stop got on

    # Calculate the number of people at the third stop
    current_count -= 18 # 18 people got off
    current_count += 2 # 2 people got on

    # Display the current number of people on the trolley
    result = current_count
    return result

print(solution())