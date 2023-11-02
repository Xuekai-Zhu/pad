def solution():
    lizzy_money = 30  # initial amount Lizzy had
    loan_amount = 15  # amount Lizzy loaned to her friend
    returned_amount = loan_amount * 1.2  # amount Lizzy's friend returned with 20% interest
    lizzy_money = lizzy_money - loan_amount + returned_amount  # new total amount of money Lizzy has
    result = lizzy_money
    return result

print(solution())