def solution():
    sack = 300  # number of potatoes in the sack
    gina = 69  # number of potatoes given to Gina
    tom = 2 * gina  # number of potatoes given to Tom, twice as much as Gina
    anne = tom / 3  # number of potatoes given to Anne, one-third of what Tom received
    remaining_potatoes = sack - gina - tom - anne  # potatoes left in the sack
    result = remaining_potatoes
    return result

print(solution())