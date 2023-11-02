def solution():
    # Calculate the number of marbles Betty gave to Stuart
    betty_gave = 0.4 * 60

    # Calculate the number of marbles Stuart had after receiving Betty's marbles
    stuart_now_has = 80

    # Calculate the number of marbles Stuart had initially
    stuart_initially_had = stuart_now_has - betty_gave
    result = stuart_initially_had
    return result

print(solution())