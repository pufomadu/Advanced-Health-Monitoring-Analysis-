def filter_nondigits(data: list) -> list:
    """
    Takes a list of strings, filters out non-digit entries, and returns a list of integers.

    Args:
        data (list[string]): list of strings representing heart rate sample data in text file

    Returns:
        list[int]): list of integers representing heart rate samples
    """

    filtered_data = []
    for item in data:
        item = item.strip()
        if item.isdigit(): 
            num = int(item)
            filtered_data.append(num) 
    return filtered_data
    
