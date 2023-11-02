def solution():
    total_amount = 124600
    amount_given_to_shelby = total_amount / 2
    remaining_amount = total_amount - amount_given_to_shelby
    number_of_grandchildren = 10
    amount_per_grandchild = remaining_amount / number_of_grandchildren
    result = amount_per_grandchild
    return result

print(solution())