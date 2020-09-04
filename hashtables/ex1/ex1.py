def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length < 2:
        return None
    cache = {}
    for i in range(len(weights)):
        if weights[i] not in cache:
            cache[weights[i]] = i
        else:
            cache[weights[i]] = [cache[weights[i]]] +[i]
    # print(cache)
    for i in range(len(weights)):
        # print(weights[i])
        if limit - weights[i] in cache:
            # print('found', (i, cache[limit -weights[i]]))
            z = cache[limit - weights[i]]
            if isinstance(z, list):
                for x in z:
                    # print('x', x)
                    if x != i:
                        z = x
            # cache[limit -weights[i]] = z if z else cache[limit -weights[i]] 
            # print(cache[limit -weights[i]], z)
            if i > z:
                return (i, z)
            else:
                return (z, i)
    return None