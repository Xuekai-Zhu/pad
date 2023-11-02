def solution():
    words_per_minute = 60  # Emily can type 60 words per minute
    words_to_write = 10800  # number of words Emily needs to write
    minutes_to_write = words_to_write / words_per_minute  # number of minutes needed to write all the words
    hours_to_write = minutes_to_write / 60  # number of hours needed to write all the words
    result = hours_to_write
    return result

print(solution())