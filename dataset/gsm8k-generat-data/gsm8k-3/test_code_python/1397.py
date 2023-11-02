def solution():
    """Marly is making soup. He adds 2 quarts of milk and three times as much chicken stock to 1 quart of pureed vegetables. Then he divides the soup into bags that can hold 3 quarts each. How many bags does he need?"""
    # Calculate the amount of chicken stock added to the soup
    stock = 3 * 1  # three times as much chicken stock as vegetables puree

    # Calculate the total amount of liquid in the soup
    total_liquid = stock + 2  # 2 quarts of milk added to the soup

    # Calculate the number of bags needed to hold the soup
    bags = total_liquid // 3

    # If there is any remaining liquid, add an extra bag
    if total_liquid % 3 != 0:
        bags += 1

    # Display the number of bags needed
    result = bags
    return result

print(solution())