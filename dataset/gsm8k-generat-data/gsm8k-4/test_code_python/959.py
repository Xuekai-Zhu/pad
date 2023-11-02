def solution():
    """Janet makes 50 snowballs and her brother makes 150 snowballs. What percentage of the snowballs did Janet make?"""
    # Define the number of snowballs made by Janet and her brother
    janet_snowballs = 50
    brother_snowballs = 150

    # Calculate the total number of snowballs
    total_snowballs = janet_snowballs + brother_snowballs

    # Calculate the percentage of snowballs made by Janet
    janet_percentage = (janet_snowballs / total_snowballs) * 100

    # Return the result
    result = janet_percentage
    return result

print(solution())