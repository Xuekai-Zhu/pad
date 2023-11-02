def solution():
     initial_pay = 10
     percent_raise = 20
     percent_cut = 25
     raise_amount = initial_pay * (percent_raise / 100)
     current_pay = raise_amount + initial_pay
     pay_cut = current_pay * (percent_cut / 100)
     new_pay = current_pay - pay_cut
     result = new_pay
     return result

print(solution())