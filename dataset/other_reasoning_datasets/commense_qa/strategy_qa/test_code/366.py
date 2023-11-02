def solution():
    easter_holiday = False # Easter was not a holiday during Jesus' time
    rabbit_significance = False # Rabbits were not significant to Jesus
    if not (easter_holiday and rabbit_significance):
        result = "no" # Jesus would not understand the Easter Bunny
    else:
        result = "yes"
    return result

print(solution())