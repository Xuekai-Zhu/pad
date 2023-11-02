def solution():
    """On Sunday Alice bought 4 pints of strawberry ice cream. The next day she went back and bought three times that number of pints. On Tuesday she bought one-third of the number of pints she bought the day before. On Wednesday she returned half of the pints she bought the day before because they were expired. How many pints of ice cream did she have on Wednesday?"""
    # Define the number of pints Alice bought on Sunday
    sunday_pints = 4

    # Define the number of pints Alice bought on Monday
    monday_pints = sunday_pints * 3

    # Define the number of pints Alice bought on Tuesday
    tuesday_pints = monday_pints // 3

    # Define the number of pints Alice returned on Wednesday
    returned_pints = monday_pints // 2

    # Calculate the total number of pints Alice had on Wednesday
    wednesday_pints = sunday_pints + monday_pints + tuesday_pints - returned_pints

    # Display the total number of pints Alice had on Wednesday
    result = wednesday_pints
    return result

print(solution())