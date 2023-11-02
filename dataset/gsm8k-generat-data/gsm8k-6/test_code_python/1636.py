def solution():
    # Calculate the total time spent in history and chemistry class
    hist_chem_time = 1.5   # in hours

    # Calculate the time spent in his other classes
    other_class_time = 7.5 - hist_chem_time   # in hours

    # Calculate the average time spent in one of his other classes in minutes
    avg_class_time = (other_class_time * 60) / 5   # divide by number of classes
    result = avg_class_time
    return result

print(solution())