def solution():
    """The Eat "N Go Mobile Sausage Sandwich Shop specializes in the sale of spicy sausage sandwiches served on a toasted bun.  Each sausage sandwich comes with four strips of jalapeno pepper, one sausage patty, and a tablespoon of Stephen's famous special sauce.  If a single jalapeno pepper makes 8 slices, and the Sandwich Shop serves a sandwich every 5 minutes, how many jalapeno peppers are required by the Sandwich Shop to serve all customers during an 8-hour day?"""
    # Calculate the number of sandwiches served in a day
    sandwiches_per_day = (8 * 60) // 5 # convert 8 hours to minutes and divide by 5

    # Calculate the number of jalapeno slices needed for one sandwich
    jalapeno_slices_per_sandwich = 4 * 8 # 4 strips per sandwich and 8 slices per strip

    # Calculate the total number of jalapeno slices needed for all sandwiches in a day
    total_jalapeno_slices = sandwiches_per_day * jalapeno_slices_per_sandwich

    # Convert the number of slices to the number of jalapeno peppers
    total_jalapeno_peppers = total_jalapeno_slices // 8

    # Display the total number of jalapeno peppers needed
    result = total_jalapeno_peppers
    return result

print(solution())