def has_negatives(a):
    # create dict for numbers and a result array
    nmbr_dict = {}
    result = []

    # iterate over each num in list
    for num in a:
        # if the number is not in dict
        if num not in nmbr_dict:
            if num > 0:
                # add that number to the dict
                nmbr_dict[num] = num
                # nmbr_dict = {1:1, 2:2, 3:3, 4:4}

            elif num < 0:
                # add the negative numbers to dict
                nmbr_dict[-num] = num
        # if the num has corresponding number in the dict
        if num > 0:
            # if number is greater than 0 and
            # if the negative number is in the dict
            # add to the result array
            if -num in nmbr_dict:
                result.append(num)

        if num < 0:
            # if the number is in the dict and the number is
            # less than zero
            # check for the positive number and cancel out
            # the negative number
            if -num in nmbr_dict:
                result.append(-num)

    # return result array
    # print(nmbr_dict)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


# thought process
# there is a list of numbers
# loop through the list
# find any number that has negative and positive
# only those numbers.
