def solution():
    """Natalia is riding a bicycle for the cycling competition. On Monday she rode 40 kilometers and on Tuesday 50 kilometers. On Wednesday she rode 50% fewer kilometers than the day before. On Thursday she rode as many as the sum of the kilometers from Monday and Wednesday. How many kilometers did Natalie ride in total?"""
    # Define the number of kilometers ridden on Monday and Tuesday
    monday_km = 40
    tuesday_km = 50

    # Calculate the number of kilometers ridden on Wednesday
    wednesday_km = tuesday_km * 0.5

    # Calculate the number of kilometers ridden on Thursday
    thursday_km = monday_km + wednesday_km

    # Calculate the total number of kilometers ridden
    total_km = monday_km + tuesday_km + wednesday_km + thursday_km

    # Return the result
    result = total_km
    return result

print(solution())