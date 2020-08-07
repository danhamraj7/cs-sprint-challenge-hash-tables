def has_negatives(a):
    # create dict for numbers and a result array
    nmbr_dict = {}
    result = []

    # iterate over each num in list
    for num in a:
        # if the num is greater than 0
        # if num in nmbr_dict
        if num >= 0:
            if num in nmbr_dict:
                # add that number to the dict
                result.append(num)
                # nmbr_dict = {1:1, 2:2, 3:3, 4:4}

            else:
                nmbr_dict[num] = 1

                # add the negative numbers to dict
        else:
            negative = -num
            if negative in nmbr_dict:
                result.append(negative)
        # if the num has corresponding number in the dict
            # if the negative number is in the dict
            # add to the result array
            else:
                nmbr_dict[negative] = 1

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
