def solution():
    wooden_toy_price = 20
    hat_price = 10
    bill_amount = 100
    number_of_wooden_toys = 2
    number_of_hats = 3
    total_spent = (wooden_toy_price * number_of_wooden_toys) + (hat_price * number_of_hats)
    change_received = bill_amount - total_spent
    result = change_received
    return result

print(solution())