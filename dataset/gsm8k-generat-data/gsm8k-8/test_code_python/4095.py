def solution():
    # Calculate Pulsar's standing time
    pulsar_time = 10

    # Calculate Polly's standing time (3 times Pulsar's)
    polly_time = 3 * pulsar_time

    # Calculate Petra's standing time (1/6 of Polly's)
    petra_time = polly_time / 6

    # Calculate the total standing time
    total_time = pulsar_time + polly_time + petra_time
    result = total_time
    return result

print(solution())