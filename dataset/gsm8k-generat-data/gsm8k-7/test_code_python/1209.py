def solution():
    num_gold_bars = 60
    tax_percent = 0.1 # 10% tax
    divorce_loss_percent = 0.5 # 50% loss in divorce

    # Calculate the number of gold bars Jame uses to pay tax
    tax_bars = num_gold_bars * tax_percent

    # Calculate the number of gold bars Jame has left after paying tax
    remaining_bars = num_gold_bars - tax_bars

    # Calculate the number of gold bars Jame loses in divorce
    divorce_loss = remaining_bars * divorce_loss_percent

    # Calculate the number of gold bars Jame has left
    num_bars_left = remaining_bars - divorce_loss
    result = num_bars_left
    return result

print(solution())