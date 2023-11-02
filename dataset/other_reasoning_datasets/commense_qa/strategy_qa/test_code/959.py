def solution():
    is_publicly_traded = True
    is_accountable_to_shareholders = True
    if is_publicly_traded and is_accountable_to_shareholders:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())