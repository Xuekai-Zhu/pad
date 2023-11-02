def solution():
    amendment_num = 8
    prohibited_methods = ["cruel and unusual punishment", "barbaric methods"]
    punished_method = "crucifixion"
    if punished_method in prohibited_methods:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())