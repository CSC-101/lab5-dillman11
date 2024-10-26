import math

import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1:data.Time, time2:data.Time) -> data.Time:
    new_time = data.Time(0, 0, 0)
    seconds = time1.second + time2.second
    minutes = time1.minute + time2.minute
    hours = time1.hour + time2.hour
    new_time.second = seconds%60
    new_time.minute = minutes%60 + seconds//60
    new_time.hour = hours + minutes//60
    return new_time

# Part 4
def is_descending(list1:list[float]) -> bool:
    for idx in range(len(list1)-1):
        if list1[idx] <= list1[idx+1]:
            return False
    return True

# Part 5
def largest_between(array:list[int], lower:int, upper:int) -> int or None:
    if lower > upper or lower < 0 or upper > len(array): #returns None if lower is negative and upper is past the length of the array
        return None
    largest = lower
    for idx in range(lower, upper + 1):
        if array[idx] > array[largest]:
            largest = idx
    return largest

# Part 6
def furthest_from_origin(list1:list[data.Point]) -> None or int:
    if list1 == []:
        return None
    distances = []
    for point in list1:
        distances.append(round(math.sqrt(pow(point.x,2) + pow(point.y,2)),2))
    return largest_between(distances,0,len(distances)-1)
