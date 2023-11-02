def solution():
    """The Eat "N Go Mobile Sausage Sandwich Shop specializes in the sale of spicy sausage sandwiches served on a toasted bun. Each sausage sandwich comes with four strips of jalapeno pepper, one sausage patty, and a tablespoon of Stephen's famous special sauce. If a single jalapeno pepper makes 8 slices, and the Sandwich Shop serves a sandwich every 5 minutes, how many jalapeno peppers are required by the Sandwich Shop to serve all customers during an 8-hour day?"""
    # Define the variables
    peppers_per_slice = 1/8
    peppers_per_sandwich = 4
    sandwiches_per_minute = 60/5
    minutes_per_day = 8*60
    sandwiches_per_day = sandwiches_per_minute * minutes_per_day

    # Calculate the number of jalapeno peppers needed for all sandwiches
    total_peppers = peppers_per_sandwich * sandwiches_per_day

    # Convert the number of peppers to slices
    total_slices = total_peppers / peppers_per_slice

    # return the result
    result = total_slices
    return result

print(solution())