def solution():
    """Rachel drinks 2 glasses of water on Sunday and 4 glasses of water on Monday. Then she drinks 3 glasses of water every day for the next 4 days. One glass of water is 10 ounces of water. If Rachel wants to drink a total of 220 ounces of water in the week (Sunday to Saturday), how many glasses of water should she drink on Saturday?"""
    # Define the number of glasses of water Rachel drinks on each day
    sunday = 2
    monday = 4
    tuesday_to_friday = 3

    # Calculate the total number of glasses of water Rachel drinks from Sunday to Friday
    total_glasses = sunday + monday + (tuesday_to_friday * 4)

    # Calculate the remaining ounces of water Rachel needs to drink on Saturday
    remaining_ounces = 220 - (total_glasses * 10)

    # Calculate the number of glasses of water Rachel needs to drink on Saturday
    saturday_glasses = remaining_ounces / 10

    # Return the result rounded to the nearest integer
    result = round(saturday_glasses)
    return result

print(solution())