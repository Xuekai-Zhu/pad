def solution():
    """Marjorie works as a baker. Every day, she makes twice as many cakes as she did the day before. On the sixth day, she makes 320 cakes. How many cakes did Marjorie make on the first day?"""
    # Define the number of cakes made on the sixth day
    sixth_day_cakes = 320

    # Calculate the number of cakes made on the fifth day
    fifth_day_cakes = sixth_day_cakes / 2

    # Calculate the number of cakes made on the fourth day
    fourth_day_cakes = fifth_day_cakes / 2

    # Calculate the number of cakes made on the third day
    third_day_cakes = fourth_day_cakes / 2

    # Calculate the number of cakes made on the second day
    second_day_cakes = third_day_cakes / 2

    # Calculate the number of cakes made on the first day
    first_day_cakes = second_day_cakes / 2

    # Return the result
    result = first_day_cakes
    return result

print(solution())