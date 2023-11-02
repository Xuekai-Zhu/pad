def solution():
    selma_marbles = 50  # given that Selma has fifty marbles
    combined_marbles = selma_marbles - 5  # given that the combined number of marbles of Merill and Elliot is 5 less than Selma's
    elliot_marbles = combined_marbles // 3  # given that Elliot has half the marbles
    merill_marbles = elliot_marbles * 2  # given that Merill has twice as many marbles as Elliot

    result = merill_marbles
    return result

print(solution())