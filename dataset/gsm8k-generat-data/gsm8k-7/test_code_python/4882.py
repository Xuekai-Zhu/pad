def solution():
    num_shoppers = 480
    express_preference = 5/8
    express_shoppers = num_shoppers * express_preference
    check_out_shoppers = num_shoppers - express_shoppers
    result = check_out_shoppers
    return result

print(solution())