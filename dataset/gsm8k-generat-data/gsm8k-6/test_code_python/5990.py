def solution():
    # Calculate how many cars Oprah needs to give away to reduce her collection to 500
    cars_to_give_away = 3500 - 500

    # Calculate how many years it will take to give away the necessary number of cars
    years_to_reduce_collection = cars_to_give_away / 50  # Oprah gives away 50 cars on average per year
    result = years_to_reduce_collection
    return result

print(solution())