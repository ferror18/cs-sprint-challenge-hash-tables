# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    hs = {}
    result =[]
    for i in files:
        z = i.split('/')[-1]
        print(z)
        if z not in hs:
            hs[z] = [i]
        else:
            hs[z] += i
    # print(hs)
    for i in queries:
        if i in hs:
            result += hs[i]
    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
