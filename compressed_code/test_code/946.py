def solution():
    
    starting_weight = 300
    first_month_loss = 20
    total_loss = first_month_loss
    for i in range(2, 5):
        loss = 0.5 * first_month_loss
        total_loss += loss
        first_month_loss = loss
    extra_loss = starting_weight - 250.5 - total_loss
    result = extra_loss
    return result

print(solution())