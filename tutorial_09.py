#Name: Melissa Vaziri
#Student Number: 101366349

#Creating a function for the matrix and providing 2 arguments
def matrix(matrix_a, matrix_b):

    #Checking if the two matrices, when they are added together, have the same dimensions
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return []

    #This is providing the new matrix for the sum
    empty_list = []

    #this is essentially performing a loop in each row and column, but also connecting the elements from matrix a and b
    #then it will store the sums into a new row, and add every row to the outcome
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        empty_list.append(row)

    return empty_list


#these are the numbers for my matrix a and b
matrix_a = [[2,2], [3,4], [5,6]]
matrix_b = [[5,2], [5,4], [6,6]]

#this is the total of both matrix a and b
total = matrix(matrix_a, matrix_b)

#this will print the total
print(total)
