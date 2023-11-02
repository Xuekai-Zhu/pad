def solution():
    santa_location = "North Pole"
    send_letters_to = "Santa Claus"
    if send_letters_to == "Santa Claus" and santa_location == "North Pole":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())