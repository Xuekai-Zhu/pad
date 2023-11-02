def solution():
    """Claudia offers art classes to kids and charges $10.00 for her one-hour class.  If 20 kids attend Saturday’s class and half that many attend Sunday’s class, how much money does she make?"""
    # Define the number of kids attending each class
    saturday_kids = 20
    sunday_kids = saturday_kids / 2

    # Define the cost per hour of the class
    cost_per_hour = 10

    # Calculate the earnings from Saturday's class
    saturday_earnings = saturday_kids * cost_per_hour

    # Calculate the earnings from Sunday's class
    sunday_earnings = sunday_kids * cost_per_hour

    # Calculate the total earnings
    total_earnings = saturday_earnings + sunday_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())