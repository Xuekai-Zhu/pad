def solution():
    """In January the families visiting a national park see animals 26 times. In February the families that visit the national park see animals three times as many as were seen there in January. Then in March the animals are shyer and the families who visit the national park see animals half as many times as they were seen in February. How many times total did families see an animal in the first three months of the year?"""
    # Define the number of times animals were seen in January
    jan_animals = 26

    # Define the number of times animals were seen in February
    feb_animals = jan_animals * 3

    # Define the number of times animals were seen in March
    mar_animals = feb_animals / 2

    # Calculate the total number of times animals were seen in the first three months
    total_animals = jan_animals + feb_animals + mar_animals

    # return the result
    result = total_animals
    return result

print(solution())