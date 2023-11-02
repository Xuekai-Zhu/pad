def solution():
    """Bobby can deadlift 300 pounds at 13. When he is 18 he can deadlift 100 pounds more than 250% of his previous deadlift. How many pounds did he add per year?"""
    # Define the starting deadlift weight and the ending deadlift weight
    starting_weight = 300
    ending_weight = (250/100 * starting_weight) + 100

    # Define the starting age and the ending age
    starting_age = 13
    ending_age = 18

    # Calculate the number of years between starting age and ending age
    years = ending_age - starting_age

    # Calculate the amount of weight added per year
    weight_added_per_year = (ending_weight - starting_weight) / years

    # Round the weight added per year to the nearest integer
    result = round(weight_added_per_year)
    return result

print(solution())