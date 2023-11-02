def solution():
    new_testament_contents = ["texts related to Christianity"]
    thetan_levels = ["term used in Scientology"]
    overlap = [content for content in new_testament_contents if content in thetan_levels]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())