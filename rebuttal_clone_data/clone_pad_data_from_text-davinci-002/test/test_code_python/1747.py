def solution():
     num_marbles = 100
     percent_white = 20
     percent_black = 30
     percent_color = 100 - percent_white - percent_black
     num_white = num_marbles * (percent_white / 100)
     num_black = num_marbles * (percent_black / 100)
     num_color = num_marbles * (percent_color / 100)
     white_price = 0.05
     black_price = 0.10
     color_price = 0.20
     total_price = (num_white * white_price) + (num_black * black_price) + (num_color * color_price)
     result = total_price
     return result

print(solution())