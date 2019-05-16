def invert_dictionary(dictionary):
    """Invert a dictionary.
    NOTE: if the values of the dictionary are not unique, the function returns the one of the mappings
    
    Args: 
        dictionary (dict): A dictionary
    
    Returns:
        dict: inverted dictionary
    
    Examples:
        >>> d = {"a": 1, "b": 2}
        >>> d_inv = invert_dictionary(d)
        >>> json.dumps(d_inv, sort_keys=True)
        '{"1": "a", "2": "b"}'
    """
    return {v: k for k, v in dictionary.items()}
