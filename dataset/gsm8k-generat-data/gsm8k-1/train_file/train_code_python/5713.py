def solution():
    """The Eat "N Go Mobile Sausage Sandwich Shop specializes in the sale of spicy sausage sandwiches served on a toasted bun. Each sausage sandwich comes with four strips of jalapeno pepper, one sausage patty, and a tablespoon of Stephen's famous special sauce. If a single jalapeno pepper makes 8 slices, and the Sandwich Shop serves a sandwich every 5 minutes, how many jalapeno peppers are required by the Sandwich Shop to serve all customers during an 8-hour day?"""
    jalapeno_slices_per_pepper = 8
    jalapeno_strips_per_sandwich = 4
    sandwiches_per_minute = 12
    minutes_per_day = 8 * 60
    total_customers = sandwiches_per_minute * minutes_per_day
    total_jalapeno_strips = total_customers * jalapeno_strips_per_sandwich
    total_jalapeno_peppers = total_jalapeno_strips / jalapeno_slices_per_pepper
    result = total_jalapeno_peppers
    return result

print(solution())