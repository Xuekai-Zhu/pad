def solution():
    nancy_drew_amateur = True
    nancy_drew_paid = False
    if not nancy_drew_paid and nancy_drew_amateur:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())