def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= len(signature):
        return signature[:n]
    
    tribonacci_sequence = signature[:]
    while len(tribonacci_sequence) < n:
        next_number = sum(tribonacci_sequence[-3:])
        tribonacci_sequence.append(next_number)

    return tribonacci_sequence

#Example Usage

signature_1 = [1, 1, 1]
n_1 = 9
result_1 = tribonacci(signature_1, n_1)
print(result_1)  # Output: [1, 1, 1, 3, 5, 9, 17, 31, 57]
