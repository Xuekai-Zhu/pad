def solution():
    
    # Define the number of periods and extra classes
    num_periods = 6
    num_extra_classes = 2

    # Define the length of each class in minutes
    class_length = 40

    # Calculate the total length of all classes in minutes
    total_class_length = num_periods * class_length * 5

    # Calculate the total time spent on Saturday and Sunday
    saturday_sunday_time = total_class_length / 16

    # Calculate the total time spent learning in a week
    total_learning_time = (saturday_sunday_time + saturday_sunday_time) * 5

    # Convert the total learning time to hours
    total_learning_hours = total_learning_time / 60

    # return the result
    result = total_learning_hours
    return result

print(solution())