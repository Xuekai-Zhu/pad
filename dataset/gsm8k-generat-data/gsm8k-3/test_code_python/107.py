def solution():
    """There is very little car traffic on Happy Street. During the week, most cars pass it on Tuesday - 25. On Monday, 20% less than on Tuesday, and on Wednesday, 2 more cars than on Monday. On Thursday and Friday, it is about 10 cars each day. On the weekend, traffic drops to 5 cars per day. How many cars travel down Happy Street from Monday through Sunday?"""
    # Define the number of cars passing on Tuesday
    tuesday_cars = 25

    # Calculate the number of cars passing on Monday
    monday_cars = tuesday_cars * 0.8

    # Calculate the number of cars passing on Wednesday
    wednesday_cars = monday_cars + 2

    # Calculate the total number of cars passing from Monday to Friday
    weekday_cars = monday_cars + tuesday_cars + wednesday_cars + 10 + 10

    # Calculate the total number of cars passing from Monday to Sunday
    total_cars = weekday_cars + 5 + 5

    # Return the result
    result = total_cars
    return result

print(solution())