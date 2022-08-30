



def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp



def pivot(my_list, pivot_index, end_index):
# end_index is the last index number of the my_list

    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
    # range(a,b), cannot take b out
    
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
            # swap(my_list, 0, 0) equal to not swap
            
    swap(my_list, pivot_index, swap_index)
    return swap_index
    # take out the index, not the value







def quick_sort_helper(my_list, left, right):
    if left < right:
    # look up above the method pivot(), "left" equal to pivot_index, "right" equal to end_index
    
        pivot_index = pivot(my_list, left, right)
        # pivot_index is the swap_index
        
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
        # the pivot_index is lay on the middle of the my_list
        
    return my_list
    # if the my_list has only one number, return it




def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)







'''
# swap a same index:
my_list3 = [1,2]
swap(my_list3,0,1)
print(my_list3)
swap(my_list3,0,1)
print(my_list3)
swap(my_list3,0,0)
print(my_list3)




my_list = [4,6,1,7,3,2,5]
my_list2 = [4,1,6,7,3,2,5]
print(pivot(my_list, 0, 6))
print(pivot(my_list2, 0, 6))
print(my_list)
print(my_list2)

print()
print(quick_sort([4,6,1,7,3,2,5]))
'''