def calculate_matrix_exponential(A, epsilon):
    n = 0
    exp_A = identity_matrix(A.shape[0])  # Initialize the result with the identity matrix
    term = exp_A.copy()  # Initialize the first term with the identity matrix

    while True:
        n += 1
        term = multiply_matrices(term, A) / n  # Calculate the next term in the series
        exp_A += term  # Add the term to the result

        # Check if the remainder is smaller than epsilon
        remainder = calculate_lagrange_form(term, A, n)
        if remainder < epsilon:
            break

    return exp_A

def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def multiply_matrices(A, B):
    n = len(A)
    m = len(B[0])
    result = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def calculate_lagrange_form(term, A, n):
    remainder = multiply_matrices(term, A) / (n + 1)
    return remainder

# Example usage
A = [[1, 2], [3, 4]]  # Replace with your own matrix
epsilon = 1e-6

exp_A = calculate_matrix_exponential(A, epsilon)
print(exp_A)