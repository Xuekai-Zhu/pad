def solution():
    # Calculate the total number of cotton candies given to Cersei's brother and sister
    candies_given = 5 + 5  

    # Calculate the number of cotton candies left after giving to brother and sister
    candies_left = 50 - candies_given  

    # Calculate the number of cotton candies given to Cersei's cousin
    candies_to_cousin = candies_left / 4  

    # Calculate the total number of candies left after Cersei gave some to her cousin and ate 12
    candies_left = candies_left - candies_to_cousin - 12  

    result = candies_left
    return result

print(solution())