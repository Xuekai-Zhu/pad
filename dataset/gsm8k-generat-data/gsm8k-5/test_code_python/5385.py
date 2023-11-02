def solution():
    ratio_boys_girls = 3/4  # Ratio of boys to girls is 3:4
    num_girls = 60  # There were 60 girls at the dance

    # Calculate the number of boys at the dance
    num_boys = int(num_girls / ratio_boys_girls)

    # Calculate the number of teachers at the dance
    num_teachers = int(num_boys * 0.2)

    # Calculate the total number of people at the dance
    total_people = num_boys + num_girls + num_teachers
    result = total_people
    return result

print(solution())