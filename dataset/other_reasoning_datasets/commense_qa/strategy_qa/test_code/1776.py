def solution():
    pennies_used_historically = True
    pennies_stopped_minting = True
    if pennies_used_historically and not pennies_stopped_minting:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())