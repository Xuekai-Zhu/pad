def solution():
    """Bobby can deadlift 300 pounds at 13.  When he is 18 he can deadlift 100 pounds more than 250% of his previous deadlift.  How many pounds did he add per year?"""
    # Define Bobby's starting deadlift weight and age
    start_weight = 300
    start_age = 13

    # Define Bobby's ending deadlift weight and age
    end_weight = (start_weight * 2.5) + 100
    end_age = 18

    # Calculate the total weight increase and the number of years between the starting and ending ages
    weight_increase = end_weight - start_weight
    year_difference = end_age - start_age

    # Calculate the average weight added per year
    weight_added_per_year = weight_increase / year_difference

    # Display the result
    result = weight_added_per_year
    return result

print(solution())