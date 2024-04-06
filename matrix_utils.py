def transpose_matrix(matrix):
    """
    Transpose the given 2D list (matrix) of numbers.

    Parameters:
        matrix (list): A 2D list (matrix) of numbers.

    Returns:
        list: The transposed matrix.
    """
    # Calculate the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the transposed values
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate over each element in the original matrix and assign it to the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix