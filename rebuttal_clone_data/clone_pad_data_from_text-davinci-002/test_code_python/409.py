def solution():
     total_cars_needed = 50
     cars_sold_first_three_days = 5 * 3
     cars_sold_next_four_days = 3 * 4
     cars_sold_so_far = cars_sold_first_three_days + cars_sold_next_four_days
     cars_needed_to_sell = total_cars_needed - cars_sold_so_far
     result = cars_needed_to_sell
     return result

print(solution())