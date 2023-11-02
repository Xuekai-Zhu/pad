def solution():
    """The Eat "N Go Mobile Sausage Sandwich Shop specializes in the sale of spicy sausage sandwiches served on a toasted bun. Each sausage sandwich comes with four strips of jalapeno pepper, one sausage patty, and a tablespoon of Stephen's famous special sauce. If a single jalapeno pepper makes 8 slices, and the Sandwich Shop serves a sandwich every 5 minutes, how many jalapeno peppers are required by the Sandwich Shop to serve all customers during an 8-hour day?"""
    peppers_per_slice = 1/8
    slices_per_sandwich = 4
    sandwiches_per_hour = 60/5
    sandwiches_per_day = sandwiches_per_hour * 8
    slices_per_day = sandwiches_per_day * slices_per_sandwich
    peppers_per_day = slices_per_day * peppers_per_slice
    result = peppers_per_day
    return result

print(solution())