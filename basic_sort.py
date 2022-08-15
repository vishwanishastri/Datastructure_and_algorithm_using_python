#Bubble sort using python
# Big O => O(n^2)

def bubble_sort(my_list):
    for i in range(len(my_list)- 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


op = bubble_sort([4,5,8,10,3])
print(op)


#selection sort = bubble sort + indexes of list should be taken care
#keep track of index where minimum value of list is stored by iterating over each in list.
# In selection sort instead of iterating over length of list will iterate over indexes and check the smallest out of all.
# Big O => O(n^2)
def selection_sort(my_list):
    # i represent index
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([5,2,4,10,9]))

#insertion sort
# we always start with 2nd item of list and compare it with item before it 
# if its less then we sway and if its not less then will not move it
#best scnario ==> already sorted list only few part needs to be sorted
# for best scenario Big O => O(n) whereas for normal case it is Big O => O(n^2)
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -=1
    return my_list



print(insertion_sort([8,9,5,4,3]))

# All three sorting method has O(1) space complexity
        
                 

