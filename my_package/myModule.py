def top_n (items, n):
    """ Returns the top n items in an array in a descending order.

    args:
        items (array): list or array-like object.
        n (int): number of items to return.
        
     return:
        array: Top n items in desc order.
    
    Egs:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]   
    """
    # We add the body of the function just below the docstring:
    
    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # If this item is bigger than next the item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!
                
    # Get last two items
    top_n = items[-n:]
    
    # Return in descending order
    return top_n[::-1]