def solution():
    """Heather made four times as many pizzas as Craig made on their first day at work at Mr. Pizza Inns. 
    On their second day, Heather made 20 fewer pizzas than Craig's number. 
    If Craig made 40 pizzas on their first day and 60 more pizzas on their second day than their first day, 
    calculate the total number of pizzas the two made together in the two days."""
    craig_day1 = 40
    craig_day2 = 40 + 60
    heather_day1 = 4 * craig_day1
    heather_day2 = craig_day2 - 20
    total_pizzas = craig_day1 + craig_day2 + heather_day1 + heather_day2
    result = total_pizzas
    return result

print(solution())