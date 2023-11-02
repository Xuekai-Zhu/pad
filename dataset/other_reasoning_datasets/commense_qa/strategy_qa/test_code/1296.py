def solution():
    meat_restrictions = ["red meat", "chicken"]
    cheese_restrictions = []
    pescatarian = True
    if pescatarian and "anchovy" not in meat_restrictions and "anchovy" not in cheese_restrictions:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())