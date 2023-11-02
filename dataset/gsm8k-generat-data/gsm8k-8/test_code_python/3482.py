def solution():
    # Calculate the number of candies given to Cersei's siblings
    num_given_away = 5 + 5
    # Subtract the number of candies given away and the ones Cersei ate from the total
    candies_left = 50 - num_given_away - 12
    # Divide by 4 to find the number of candies given to her cousin
    candies_to_cousin = candies_left / 4
    # Subtract the number of candies given to the cousin from the total to get the final answer
    result = candies_left - candies_to_cousin
    return result

print(solution())