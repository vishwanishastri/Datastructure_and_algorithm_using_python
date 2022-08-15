# Merge sort using Python
# To combine 2 sorted list is easier so merge sort
# divides list into equal part , sorts it and then merge all
#space complexity => O(n)
#Time complexity => O(nlogn) = O(n) for iterating and logn for combining
def merge_sort(list1, list2):
    #list1 and list2 should be presorted (Mandatory)
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i +=1
        else:
            combined.append(list2[j])
            j +=1
    while i < len(list1):
        combined.append(list1[i])
        i +=1
    while j < len(list2):
        combined.append(list2[j])
        j +=1
    return combined

print(merge_sort([2,4,7,8,9], [2,4,8,9,10]))

#space complexity(breaking and creating new list doubles memory use) => O(n) 
#time complexity => O(nlogn)
def merge_sort_with_single_list(my_list):
    #break lists in half using recursion
    #base case: when len(list) is 1
    # use merge to put it back in final list
    if len(my_list) ==1:
        return my_list
    mid = int(len(my_list)/2) #convert float to int
    left = my_list[:mid]
    right = my_list[mid:]
    return merge_sort(merge_sort_with_single_list(left), merge_sort_with_single_list(right))


print(merge_sort_with_single_list([2,4,7,8,9, 10, 12]))

