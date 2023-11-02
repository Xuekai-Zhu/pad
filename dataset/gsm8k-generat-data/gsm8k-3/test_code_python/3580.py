def solution():
    """Remi planted tomato seedlings on his farm, starting with 200 on the first day and twice as many on the second day. After two days, he and his father transferred a total of 1200 seedlings. How many seedlings did Remi's father plant?"""
    # Calculate the number of seedlings planted on the first and second days
    first_day_plants = 200
    second_day_plants = 2 * first_day_plants

    # Calculate the total number of seedlings planted by Remi
    total_plants = first_day_plants + second_day_plants

    # Calculate the number of seedlings planted by Remi's father
    father_plants = 1200 - total_plants

    # Display the number of seedlings planted by Remi's father
    result = father_plants
    return result

print(solution())