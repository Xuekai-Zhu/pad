def solution():
     total_slices = 78
     buzz_slices = 5
     waiter_slices = 8
     buzz_ratio = 5
     waiter_ratio = 8
     buzz_actual = total_slices * (buzz_ratio / (buzz_ratio + waiter_ratio))
     waiter_actual = total_slices * (waiter_ratio / (buzz_ratio + waiter_ratio))
     result = int(waiter_actual - 20)
     return result

print(solution())