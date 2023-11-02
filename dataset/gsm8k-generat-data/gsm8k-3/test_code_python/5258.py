def solution():
    """Jim decides he wants to practice for a marathon coming up. He starts off by running 5 miles every day for 30 days straight. He then pushes himself to run 10 miles a day for the next 30 days. Finally, as marathon day gets closer Jim runs 20 miles a day for 30 days straight. How many miles does Jim run in total during the 90 days?"""
    # Define the number of miles Jim runs per day for each period
    MILES_DAY1 = 5
    MILES_DAY2 = 10
    MILES_DAY3 = 20

    # Calculate the total miles Jim runs in each period
    miles1 = MILES_DAY1 * 30
    miles2 = MILES_DAY2 * 30
    miles3 = MILES_DAY3 * 30

    # Calculate the total miles Jim runs in 90 days
    total_miles = miles1 + miles2 + miles3

    # Display the total miles Jim runs in 90 days
    result = total_miles
    return result

print(solution())