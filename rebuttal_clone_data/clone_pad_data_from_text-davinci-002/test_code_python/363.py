def solution():
    tony_paid = 7
    tony_apples = 2
    tony_bananas = 1
    arnold_paid = 5
    arnold_apples = 1
    arnold_bananas = 1
    cost_per_apple = (tony_paid - arnold_paid) / (tony_apples - arnold_apples)
    cost_per_banana = tony_paid - (tony_apples * cost_per_apple)
    result = cost_per_banana
    return result

print(solution())