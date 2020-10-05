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


# 1.Initializingres with the first list inside the array
# 2.Iterating through the array containing lists
# 3.Updating the res list by applying intersection_update() function to check the common elements.
# 4.Finally returning the list and display the output by the help of the print statement.

# https://www.geeksforgeeks.org/python-dictionary-intersection-find-common-elements-three-sorted-arrays/