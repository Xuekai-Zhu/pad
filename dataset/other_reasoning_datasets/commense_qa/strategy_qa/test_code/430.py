def solution():
    oprah_winfrey_net_worth = 1000000000
    bugatti_cost = 3000000
    number_of_staff = 24
    total_cost = bugatti_cost * number_of_staff
    if oprah_winfrey_net_worth > total_cost:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())