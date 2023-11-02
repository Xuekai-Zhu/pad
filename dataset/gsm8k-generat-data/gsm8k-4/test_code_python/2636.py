def solution():
    """At school today, Charlize was 20 minutes late. Four of her classmates were each ten minutes late than she was. What's the total time for which the five students were late?"""
    # Define the initial lateness of Charlize
    charlize_late = 20

    # Define the lateness of Charlize's classmates
    classmates_late = [charlize_late + 10] * 4

    # Compute the total lateness of all five students
    total_late = sum(classmates_late) + charlize_late

    # return the result
    result = total_late
    return result

print(solution())