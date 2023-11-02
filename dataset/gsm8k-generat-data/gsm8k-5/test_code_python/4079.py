def solution():
    bread_cost = 2  # Each loaf of bread costs $2
    milk_cost = 2  # Each carton of milk costs $2
    total_cost = (4 * bread_cost) + (2 * milk_cost)  # Clare bought 4 loaves of bread and 2 cartons of milk
    remaining_money = 47 - total_cost  # Clare started with $47

    result = remaining_money
    return result

print(solution())