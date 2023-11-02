def solution():
    balloons_on_string = 3 * 12  # The clown has 3 dozen balloons on a string in his hand
    balloons_bought = 3 + 12  # 3 boys and 12 girls buy a balloon each
    balloons_remaining = balloons_on_string - balloons_bought  # Calculate how many balloons the clown is still holding
    result = balloons_remaining
    return result

print(solution())