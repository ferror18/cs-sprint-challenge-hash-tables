def intersection(arrays):
    """
    YOUR CODE HEREaaa
    """
    # Your code here
    result = []
    counter = {}
    for i in arrays:
        unique = {}
        for x in i:
            if x not in unique:
                unique[x] = 1
        for i in unique.items():
            if i[0] in counter:
                counter[i[0]] += 1
            else:
                counter[i[0]] = 1
    # print('counter',counter)
    for i in counter.items():
        if i[1] == len(arrays):
            result.append(i[0])
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
