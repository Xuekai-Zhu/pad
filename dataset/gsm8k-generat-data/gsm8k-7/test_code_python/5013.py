def solution():
    num_staplers = 50
    num_reports = 36 * 3

    # Calculate the total number of staples used
    total_staples = num_reports

    # Calculate the number of staplers left in the stapler
    num_staplers_left = num_staplers - (total_staples // 100)

    result = num_staplers_left
    return result

print(solution())