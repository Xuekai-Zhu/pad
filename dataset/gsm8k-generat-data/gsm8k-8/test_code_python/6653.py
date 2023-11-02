def solution():
    # Calculate the total cups of sugar
    total_sugar = 3 + (2*6)

    # Calculate the number of cupcakes she can make with the available sugar
    cupcakes = total_sugar // 1 * 12

    # Calculate the number of cupcakes she can frost with the available sugar
    frosted_cupcakes = total_sugar // 2 * 12

    # Calculate the lesser of the two quantities to get the final answer
    final_answer = min(cupcakes, frosted_cupcakes)

    return final_answer // 12

print(solution())