def get_indices_of_item_weights(weights, length, limit):
    # create a dictionary of the weights
    # returns a tuple
    weights_dict = dict()

    # iterate
    for i in range(length):
        # if a k:v pair is in the dictionary
        # and is equal to the remainder
        #  minus the curr ele from limit
        x = weights_dict.get(limit - weights[i])
        # if the value is found at the index in the dict

        if x is not None:
            # return tuple with the corresponding index
            return (i, x)

        else:
            # if it is not found, set key as the curr
            # val from list and val as the found index
            weights_dict[weights[i]] = i

    print(weights_dict)

    # when the sum of the num in the list
    # is not the limit, return none.
    return None
