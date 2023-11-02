def solution():
     PingPongBalls_price = .10
     discount_Percentage = .30
     numberOfBallsBought = 10000
 
    costAfterDiscount = (1-discount_Percentage) * PingPongBalls_price * numberOfBallsBought
    result = costAfterDiscount
    return result

print(solution())