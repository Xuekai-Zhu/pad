def solution():
    """At school today, Charlize was 20 minutes late. Four of her classmates were each ten minutes late than she was. What's the total time for which the five students were late?"""
    charlize = 20
    classmates = [charlize + 10] * 4
    total_lateness = charlize + sum(classmates)
    result = total_lateness
    return result

print(solution())