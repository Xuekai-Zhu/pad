def solution():
    apples_bought = 55
    apples_given = 10
    apples_remaining = apples_bought - apples_given
    people = 5
    apples_for_each = apples_remaining / people
    result = apples_for_each
    return result

print(solution())