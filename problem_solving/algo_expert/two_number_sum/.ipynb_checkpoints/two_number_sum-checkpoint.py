def two_number_sum_1(array, target):
    '''
    Find the two numbers in the array which sum to the target.
    '''
    
    n = len(array)
    
    for i in range(n-1):
    firstNum = array[i]
        for j in range(i+1, n):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [secondNum, firstNum]
    
    return []

