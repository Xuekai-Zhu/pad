def solution():
    # Find the percentage of girls in the class
    percent_girls = 100 - 40  # assuming there are only boys and girls in the class

    # Calculate the class average on the math test
    class_avg = (40 * 0.8 + percent_girls * 0.9) / 100
    result = class_avg
    return result

print(solution())