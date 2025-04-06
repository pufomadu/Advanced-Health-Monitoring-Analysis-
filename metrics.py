#Import the math module to use the sqrt function
import math

def average(data: list) -> float:
    """
    Calculates the average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    # Check if the data list is empty and return it as is, this is to avoid division by zero error
    if not data:
        return data
    
    # Calculate the average 
    average = 0
    sum = 0
    for num in data:
        sum += num
    average = sum / len(data)
    return round(average, 2)
    


def maximum(data: list) -> float:
    """
    Calculates the maximum value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the maximum number in this list rounded to 2 decimal places
    """
    # Check if the data list is empty and return it as is, this is to avoid division by zero error
    if not data:
        return data
    
    # Identify the max value in the list
    max_value = data[0] 
    for num in data:
        if num >= max_value:
            max_value = num
    return round(max_value, 2)


def variance(data: list) -> float:
    """
    Calculates the population variance of the list of data.
        
    Variance measures how the data points differ from the mean; it is calculated as the average of the squared differences from the mean.
    
    This function calls the 'average()' function to calculate the mean.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the population variance rounded to 2 decimal places
    """
    # Check if the data list is empty and return it as is, this is to avoid division by zero error
    if not data:
        return data
    
    # Calculate the mean using the average function and then calculate the variance
    mean = average(data)  
    squared_diffs = 0
    
    for num in data: 
        squared_diffs += (num - mean) ** 2
    
    var = squared_diffs / len(data)
    return round(var, 2)


def standard_deviation(data: list) -> float:
    """
    Calculates the population standard deviation of the list of data.
    
    The standard deviation measures how spread out the values are from the mean; it is calculated as the square root of the variance.
            
    This function calls the 'variance()' function to calculate the varaiance.

     Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the population standard deviation rounded to 2 decimal places
    """
    # Check if the data list is empty and return it as is, this is to avoid division by zero error
    if not data:
        return data
    
    # First calculate the variance by calling the 'variance()' function, then the standard deviation is calculated as the square root of the variance.
    var = variance(data)
    st_dev = math.sqrt(var)
    return round (st_dev, 2)
