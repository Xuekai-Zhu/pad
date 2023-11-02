def solution():
    # Calculate the total length of time that the three entertainers stand on their back legs
    pulsar_time = 10  # Pulsar stands on his back legs for 10 minutes
    polly_time = pulsar_time * 3  # Polly stands on her back legs for three times as long as Pulsar
    petra_time = polly_time / 6  # Petra stands on his back legs for one-sixth as long as Polly
    total_time = pulsar_time + polly_time + petra_time
    result = total_time
    return result

print(solution())