#Quick sort using Python
#start with pivot point and then compare numbers after that
# if less than pivot point , swap it
#Big O --> pivot (O(n)) + O(2^3) ~ O(logn) == O(nlogn)
# worst case(already sorted data after pivot) --> O(n^2)
#If data is already sorted then use insertion sort as its Big O is O(n) for worst case
# for unsorted use quick sort or merge sort

#input = [4,6,1,7,3,2,5]
#after pivot = [2,1,3,4,6,7,5]
def pivot(my_list, pivot_index, end_index):
    # returns index so that quick sort can be applied to both side of list except on that index
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index +=1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def quick_sort_helper(my_list, left, right):
    #Runs recursively pivot function on both side of list
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)


print(quick_sort([4,6,1,7,3,2,5]))