#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    hs = {}
    # for i in tickets:
    #     route.append(i.destination)
    for i in tickets:
        hs[i.source] = i.destination
    print(hs)
    current = 'NONE'
    route.append(hs[current])
    while hs[current] != 'NONE':
        current = hs[current]
        route.append(hs[current])
    # print(f'Mine{route}\nrequired{["LAX", "SFO", "BHM", "FLG", "XNA", "SAP","SLC", "PIT", "ORD", "NONE"]}')
    return route
