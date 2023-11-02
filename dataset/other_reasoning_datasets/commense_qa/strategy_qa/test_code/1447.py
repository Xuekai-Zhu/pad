def solution():
    start_date = "July 14, 1969"
    end_date = "July 20, 1969"
    duration = (datetime.strptime(end_date,'%B %d, %Y') - datetime.strptime(start_date,'%B %d, %Y')).days
    if duration >= 30:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())