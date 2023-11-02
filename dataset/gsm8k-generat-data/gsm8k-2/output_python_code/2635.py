def solution():
    """At school today, Charlize was 20 minutes late. Four of her classmates were each ten minutes late than she was. What's the total time for which the five students were late?"""
    charlize_time = 20
    classmates_time = [charlize_time + 10 for i in range(4)]
    total_time = charlize_time + sum(classmates_time)
    result = total_time
    return result

print(solution())