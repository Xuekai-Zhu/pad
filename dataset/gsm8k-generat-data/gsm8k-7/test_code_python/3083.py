def solution():
    total_marbles = 100
    white_percent = 0.2
    black_percent = 0.3
    white_price = 0.05
    black_price = 0.1
    color_price = 0.2

    # Calculate the number of white marbles and the amount earned from selling them
    num_white = total_marbles * white_percent
    white_earnings = num_white * white_price

    # Calculate the number of black marbles and the amount earned from selling them
    num_black = total_marbles * black_percent
    black_earnings = num_black * black_price

    # Calculate the number of colored marbles and the amount earned from selling them
    num_color = total_marbles - num_white - num_black
    color_earnings = num_color * color_price

    # Calculate the total earnings
    total_earnings = white_earnings + black_earnings + color_earnings
    result = total_earnings
    return result

print(solution())