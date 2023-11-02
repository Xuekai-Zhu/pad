def solution():
    """Jackson’s mom packs him a peanut butter and jelly sandwich for his school lunch on Wednesdays and Fridays.
    There are 36 weeks of school and Jackson has only missed 1 Wednesday and 2 Fridays.
    How many peanut butter and jelly sandwiches did he eat for lunch this school year?"""
    
    # Determine the number of sandwiches missed
    missed_sandwiches = 1 + 2
    
    # Determine the number of sandwich days (Wednesdays and Fridays) in a school year
    sandwich_days = 2 * (36 - missed_sandwiches)
    
    # Calculate the total number of sandwiches eaten
    sandwiches_eaten = sandwich_days
    
    # Display the total number of sandwiches eaten
    result = sandwiches_eaten
    return result

print(solution())