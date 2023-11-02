def solution():
    total_candies = 100  # Josh starts with 100 gummy bear candies
    siblings_candies = 10 * 3  # Josh gives 10 candies each to his 3 siblings
    remaining_candies = total_candies - siblings_candies  # Josh has remaining candies after giving some to his siblings
    friend_candies = remaining_candies / 2  # Josh gives half of the remaining candies to his friend
    josh_eats_candies = 16  # Josh eats 16 gummy bear candies
    candies_left = remaining_candies - friend_candies - josh_eats_candies  # Josh has candies left to share with others
    result = candies_left
    return result

print(solution())