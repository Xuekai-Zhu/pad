def solution():
    green_beans = 60
    sugar = green_beans - 10
    rice = green_beans + 30
    rice_lost = (rice / 3)
    sugar_lost = (sugar / 5)
    total_lost = rice_lost + sugar_lost
    remaining_stock = green_beans + sugar + rice - total_lost
    result = remaining_stock
    
    return result

print(solution())