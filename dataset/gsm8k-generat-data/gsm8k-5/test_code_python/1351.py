def solution():
    thor_sold = (200/10)-10  # Thor sold 10 less than Jake, and Quincy sold 10 times as many as Thor
    jake_sold = thor_sold + 10  # Jake sold 10 more than Thor
    quincy_sold = 200  # Quincy sold 200 stuffed animals

    # Calculate the difference between Quincy's sales and Jake's sales
    difference = quincy_sold - jake_sold
    result = difference
    return result

print(solution())