def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

    # thought process
    # given a list that contains several sub-list of integers
    # loop through all the sub-lists
    # find all the integers that repeats itself in every single
    # sublist.

    # take the first ele in the first sub-list
    # compare it to the ele in the second sub-list
    # if it is not found go to the next ele in the first-sublist
    # while the ele that is being compared is found in any sub list
    # move to the other sub- list until the end.
    # if it reaches the last sublist and the ele is found in all the
    # sublist return the ele in the dict.
