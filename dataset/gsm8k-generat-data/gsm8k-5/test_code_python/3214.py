def solution():
    initial_chickens = 400  # Carla had 400 chickens initially
    percent_died = 40  # 40% of the chickens died due to the disease
    chickens_died = initial_chickens * (percent_died / 100)  # Calculate the number of chickens that died
    chickens_bought = chickens_died * 10  # Calculate the number of chickens Carla bought

    # Calculate the total number of chickens
    total_chickens = initial_chickens - chickens_died + chickens_bought
    result = total_chickens
    return result

print(solution())