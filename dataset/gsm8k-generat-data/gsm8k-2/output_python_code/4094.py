def solution():
    """Pulsar, the shuffle-dancing bear, Polly, the pink prancing poodle, and Petra, the proud portly pachyderm, are entertainers at the Big Top Circus. In one show, Pulsar stands on his two back legs for a total of 10 minutes. Then, Polly stands on her back legs for three times as long as Pulsar. And then, finally, Petra stands of his back legs for one-sixth as long as Polly. What is the combined length of time, in minutes, that the three entertainers stand on their back legs?"""
    pulsar_time = 10
    polly_time = 3 * pulsar_time
    petra_time = polly_time / 6
    total_time = pulsar_time + polly_time + petra_time
    result = total_time
    return result

print(solution())