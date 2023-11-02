def solution():
    initial_temperature = 41
    temperature_increase = 3
    final_temperature = 212
    pasta_cooking_time = 12
    mixing_and_salad_time = pasta_cooking_time / 3
    total_time = final_temperature - initial_temperature + pasta_cooking_time + mixing_and_salad_time
    result = total_time
    return result

print(solution())