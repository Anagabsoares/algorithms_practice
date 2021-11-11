''' MULTIPLE POINTERS'''
# ! Creating pointers or values that correspond to an index
#!  and move towards the beginning end or middle based on a certain 
#! conditional condition.
# !VERY efficient for solving the problems with minimal 
# !space complexity as well.


'''Exercise: SUMZERO find the first pairs that when summed is ==0'''

def sumzero(array):
    for item in range(len(array)):
        for j in range(1,len(array)):
            if array[item] + array[j] ==0:
                return [array[item], array[j]]
            j +=1
#Not a good solution because we have nested loop O(n^2)  
    



def sum_zero(arr):
    left =0 #we will add 1 every time
    right= len(arr) -1 #we will decrease the value each time
    while left < right:
        sum_values = arr[left] + arr[right]
        if sum_values == 0:
            return [arr[left], arr[right]]
        elif sum_values > 0:
            right -=1
        else:
            left +=1



def count_unique_values(array):
    # it needs to be sorted 
    i= 0
    
    for item in range(1,len(array)):
        if array[i] != array[item]:
            i +=1
            array[i]= array[item]
    return i +1 if array else 0


print(count_unique_values([1,2,2,3]))