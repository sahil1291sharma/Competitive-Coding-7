def meetingRooms(interval):
  interval.sort()

  count = 1
  for i in range(1, len(interval)):
    if interval[i][0] < interval[i-1][1]:
      count +=1

  return count

print(meetingRooms([[0,30], [5,32], [15,20], [6,16]]))
print(meetingRooms([[0,30], [5,32], [15,20], [6,9]]))

#Time complexity O(NlogN)
#Space complexity O(1)