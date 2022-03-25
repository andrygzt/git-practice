def max_value(numbers):
<<<<<<< HEAD
    max = number[0]
    for num = numbers:
        if num > max:
            max = num
    return max
    
=======
    """ This function returns the largest number
        in the list.
    """
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max


>>>>>>> d0d7c8704b9aa553d1b56686129a4a2a4928f986
if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))