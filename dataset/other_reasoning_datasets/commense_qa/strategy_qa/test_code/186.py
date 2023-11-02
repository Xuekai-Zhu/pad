def solution():
    autumn_start = "September 20"
    autumn_end = "December 20"
    independence_day = "July 4"
    autumn_range = pd.date_range(start=autumn_start, end=autumn_end)
    if independence_day in autumn_range.strftime('%B %d').tolist():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())