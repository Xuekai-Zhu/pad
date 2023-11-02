def solution():
    science_minutes = 60
    math_minutes = 80
    literature_minutes = 40

    # Calculate the total minutes Sam spends studying
    total_minutes = science_minutes + math_minutes + literature_minutes

    # Convert the total minutes to hours
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())