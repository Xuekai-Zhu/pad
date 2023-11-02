def solution():
    """Boston had .5 feet of snow on the first day of winter. The next day they got an additional 8 inches. Over the next 2 days, 2 inches of the snow melted. On the fifth day, they received another 2 times the amount of snow they received on the first day. How many feet of snow do they now have?"""
    # Define the initial amount of snow in feet
    snow = 0.5

    # Add the amount of snow received on the second day in feet
    snow += 8 / 12

    # Subtract the amount of snow that melted over the next two days in feet
    snow -= 2 / 12

    # Add the amount of snow received on the fifth day in feet
    snow += 2 * 0.5

    result = round(snow, 2)
    return result

print(solution())