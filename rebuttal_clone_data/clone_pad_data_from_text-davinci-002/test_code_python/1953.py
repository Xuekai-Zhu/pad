def solution():
    model_price = 100
    models_bought_kindergarten = 2
    models_bought_elementary = models_bought_kindergarten * 2
    total_models = models_bought_kindergarten + models_bought_elementary
    percent_discount = 5
    models_bought_discount = total_models - 5
    discount_amount = model_price * (percent_discount / 100)
    total_price_paid = (models_bought_kindergarten + models_bought_elementary) * model_price - models_bought_discount * discount_amount
    result = total_price_paid
    
    return result

print(solution())