def solution():
    # Find the total number of vegetables bought by Marcel and Dale
    total_vegetables = 10 + (1/2) * 10 + 8  # Marcel buys 10 ears of corn, Dale buys half that amount (5), and 8 potatoes

    # Find the number of potatoes bought by Marcel
    marcel_potatoes = total_vegetables - 8  # Subtract Dale's 8 potatoes from the total to get Marcel's

    result = marcel_potatoes
    return result

print(solution())