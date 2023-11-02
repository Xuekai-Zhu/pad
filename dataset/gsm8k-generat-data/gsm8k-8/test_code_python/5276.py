def solution():
    # Calculate the initial number of girls and boys
    total_students = 20
    girls = int(total_students * 0.4)
    boys = total_students - girls

    # Add 5 new boys to the classroom
    new_boys = 5
    total_students += new_boys
    boys += new_boys

    # Recalculate the percentage of girls in the class
    percentage_girls = girls / total_students * 100
    result = percentage_girls
    return result

print(solution())