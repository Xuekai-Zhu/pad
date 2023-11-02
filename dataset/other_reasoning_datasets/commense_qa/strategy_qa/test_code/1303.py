def solution():
    new_testament_angels = ["Michael", "Gabriel"]
    jewish_angels = ["Michael", "Gabriel", "Uriel", "Raphael"]
    overlap = [angel for angel in new_testament_angels if angel in jewish_angels]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())