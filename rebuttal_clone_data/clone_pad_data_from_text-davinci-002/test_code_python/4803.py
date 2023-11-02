def solution():
     apples = 2
     price_per_apple = 2
     cost_of_apples = apples * price_per_apple
     pie_crust = 2
     lemon = 0.5
     butter = 1.5
     total_cost = cost_of_apples + pie_crust + lemon + butter
     cost_per_piece = total_cost / 8
     result = cost_per_piece
 
     return result

print(solution())