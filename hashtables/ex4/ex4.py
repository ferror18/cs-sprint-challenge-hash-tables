def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negatives = {}
    result = []
    for i in a:
        negatives[-i] = i
    for i in a:
        if i in negatives and i > 0:
            result.append(i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
