#  Hint:  You may not need all of these.
# Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticket_dict = {}
    for itn in range(length):
        ticket_dict[tickets[itn].source] = tickets[itn].destination

    route = []
    curr = ticket_dict["NONE"]

    # first ticket destinations source = "NONE"
    # final flight destination source = "NONE"

    while curr != "NONE":
        route.append(curr)
        curr = ticket_dict[curr]
    route.append(curr)

    return route

    # you would look for the ticket
    # where the departure is equal to your current
    # location(start airport)
    # In this case the start airport and end airport is none
    # start departure is none.
    # check the destination on that ticket.
    # that ticket destination would be the next departure.
    # do that as long as there are tickets.
    # when you reach the ticket where the destination is none
    # **YOU HAVE ARRIVED**
