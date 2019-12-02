def merge(matrix, a, b, mid):
    k = a
    l = mid + 1
    c = 0
    temp = []
    while k < mid + 1 and l < b + 1:
        if matrix[k] < matrix[l]:
            temp.append(matrix[k])
            c += 1
            k += 1
        else:
            temp.append(matrix[l])
            l += 1
            c += 1
    while k < mid + 1:
        temp.append(matrix[k])
        c += 1
        k += 1
    while l < b + 1:
        temp.append(matrix[l])
        c += 1
        l += 1

    i = 0
    while i < c:
        matrix[a + i] = temp[i]
        i += 1


def merge_sort(matrix, i, j):
    mid = int((i + j) / 2)
    if i < j:
        merge_sort(matrix, i, mid)
        merge_sort(matrix, mid + 1, j)
        merge(matrix, i, j, mid)
