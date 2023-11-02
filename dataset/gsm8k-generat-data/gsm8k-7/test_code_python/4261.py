def solution():
    total_students = 30
    num_boys = 10
    num_girls = 2 * num_boys

    boys_cups = num_boys * 5
    total_cups = 90

    # Calculate the total number of cups brought by the girls
    total_girls_cups = total_cups - boys_cups

    # Calculate the average number of cups brought by each girl
    avg_girls_cups = total_girls_cups / num_girls
    result = avg_girls_cups
    return result

print(solution())