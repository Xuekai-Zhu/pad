def solution():
    # Define the total number of scientists
    total_scientists = 70

    # Calculate the number of scientists from Europe
    europe_scientists = total_scientists / 2

    # Calculate the number of scientists from Canada
    canada_scientists = total_scientists / 5

    # Calculate the number of scientists from the USA
    usa_scientists = total_scientists - europe_scientists - canada_scientists

    result = usa_scientists
    return result

print(solution())