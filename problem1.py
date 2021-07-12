#Max heap solution
def thirdSmallest( matrix, k):
    pq = []
    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            heapq.heappush(pq, -1*matrix[i][j])
            if len(pq) > k:
                heapq.heappop(pq)
    return -1*(heapq.heappop(pq))


print(thirdSmallest([[1, 5, 9],[10, 11, 13],[12, 13, 15]], 8)) #no duplicates for k value

print(thirdSmallest([[1,3,7], [5,10,12], [6, 12, 15]], 3)) #no duplicates for k value

print(thirdSmallest([[-5]], 1)) #Only 1 element 

print(thirdSmallest([[1,3,7], [3,10,12], [6, 12, 15]], 3)) # duplicates at k position


#Time complexity is O(m*nlogK)
#Space complexity is O(m*n)