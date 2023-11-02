def solution():
    """Paul is working at a university. He is part of a big project, which involves 70 scientists in total. Half of them are from Europe and one-fifth are from Canada. The rest are from the USA. How many scientists in this project are from the USA?"""
    # Define the total number of scientists
    total_scientists = 70

    # Calculate the number of scientists from Europe
    europe_scientists = total_scientists // 2

    # Calculate the number of scientists from Canada
    canada_scientists = total_scientists // 5

    # Calculate the number of scientists from the USA
    usa_scientists = total_scientists - europe_scientists - canada_scientists

    # Display the number of scientists from the USA
    result = usa_scientists
    return result

print(solution())