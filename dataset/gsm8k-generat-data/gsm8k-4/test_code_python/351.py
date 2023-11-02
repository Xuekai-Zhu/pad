def solution():
    """Jackson’s mom packs him a peanut butter and jelly sandwich for his school lunch on Wednesdays and Fridays. There are 36 weeks of school and Jackson has only missed 1 Wednesday and 2 Fridays. How many peanut butter and jelly sandwiches did he eat for lunch this school year?"""
    # Define the number of weeks and the number of missed days
    total_weeks = 36
    missed_days = 3

    # Calculate the total number of sandwich days
    sandwich_days = (total_weeks * 2) - missed_days

    # Calculate the number of peanut butter and jelly sandwiches eaten
    sandwiches_eaten = sandwich_days * 1

    result = sandwiches_eaten
    return result

print(solution())