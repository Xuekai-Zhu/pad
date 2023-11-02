def solution():
    receive_little_sunshine = True
    dangerous_to_expose_skin = True
    # Check if it is unlikely for Eskimos to sunbathe frequently
    if receive_little_sunshine or dangerous_to_expose_skin:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())