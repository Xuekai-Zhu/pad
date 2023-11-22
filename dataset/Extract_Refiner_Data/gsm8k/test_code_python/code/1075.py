def solution():
    
    # Define the original price of the watch
    original_price = 2000

    # Calculate the price Mr. Rogers bought the watch at 75% of its original price
    roger_price = original_price * 0.75

    # Calculate the price Mr. Roger's friend sold the watch at 120% of his original price
    friend_price = roger_price * 0.2

    # Calculate the percentage discount obtained by Mr. Roger's friend
    discount_percentage = (friend_price / original_price) * 100

    # Display the percentage discount obtained
    result = discount_percentage
    return result

print(solution())