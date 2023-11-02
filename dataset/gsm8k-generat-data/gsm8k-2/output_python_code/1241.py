def solution():
    """Vinny weighed 300 pounds then lost 20 pounds in the first month of his diet. He continued his diet but each month, he lost half as much weight as he had lost in the previous month. At the start of the fifth month of his diet, he worked harder to lose extra weight then decided to end his diet. If Vinny weighed 250.5 pounds at the end of his diet, how many pounds did he lose throughout the fifth month?"""
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