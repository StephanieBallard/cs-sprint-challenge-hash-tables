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
    cache = {}

    route = [None] * length

    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    next = cache["None"]

    for cur in range(0, length):
        route[cur] = next
        next = cache[next]

    return route
