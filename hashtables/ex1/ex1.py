def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}

    for i in range(len(weights)):
        weight = weights[i]
        pair = limit - weight
        if pair in dictionary:
            return [dictionary[pair], i]
        dictionary[weight] = i
    return None


        



# instantiate an empty dictionary
# for each number in list of numbers:
#     result = subtract number from target number
#     look for result in the dictionary (instant lookup)
#     if found:
#         return index of number and index of dictionary lookup result
#     else:
#         add number to dictionary as key with value being the index

# second_Number = limit - weights[i]
#         if(second_Number in dictionary.keys()):
#             secondIndex = weights.index(second_Number)
#             if(i != secondIndex):
#                 return sorted([i, secondIndex])
#         else:
#             dictionary.update({weights[i]: i})