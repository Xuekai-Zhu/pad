def solution():
    """Paul eats a lot when he studies. He loves sandwiches and eats them at the same rate every three days. He eats 2 sandwiches the first day, then doubles that number of sandwiches for the second day. On the third day, he doubles the number of sandwiches he ate on the second day. How many sandwiches would Paul eat if he studied 6 days in a row?"""
    sandwiches_day1 = 2
    sandwiches_day2 = sandwiches_day1 * 2
    sandwiches_day3 = sandwiches_day2 * 2
    sandwiches_per_cycle = sandwiches_day1 + sandwiches_day2 + sandwiches_day3
    cycles = 6 // 3  # Calculates how many complete cycles of 3 days Paul studies for
    leftover_days = 6 % 3  # Calculates how many extra days Paul studies for outside of complete cycles
    sandwiches_total = ((sandwiches_per_cycle * cycles) 
                        + (sandwiches_day1 + sandwiches_day2 + sandwiches_day3))  # Calculates total sandwiches for all complete cycles + extra days
    if leftover_days == 1:
        sandwiches_total += sandwiches_day1  # Adds number of sandwiches for the extra day
    elif leftover_days == 2:
        sandwiches_total += (sandwiches_day1 + sandwiches_day2)  # Adds number of sandwiches for the extra two days
    result = sandwiches_total
    return result

print(solution())