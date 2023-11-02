def solution():
    """Vinny weighed 300 pounds then lost 20 pounds in the first month of his diet. He continued his diet but each month, he lost half as much weight as he had lost in the previous month. At the start of the fifth month of his diet, he worked harder to lose extra weight then decided to end his diet. If Vinny weighed 250.5 pounds at the end of his diet, how many pounds did he lose throughout the fifth month?"""
    starting_weight = 300
    first_month_loss = 20
    total_loss = first_month_loss
    for i in range(2, 6):
        loss = first_month_loss / (2 ** (i-1))
        total_loss += loss
    end_weight = starting_weight - total_loss
    fifth_month_loss = end_weight - 250.5
    result = fifth_month_loss
    return result

print(solution())