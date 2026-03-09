# Reversing am Array : Reverse a given list of numbers.
# Modify the input array in-place and return the modified array
def insert_element_at_position(nums, element, position):
    #arr[::-1]
    #return arr

    #element = 40 #int(input("Please enter the element to insert in the Array:"))
    #pos = 4 #int(input("Please enter the position to insert in the Array:"))

    #Example 1 - test case
    #nums=[2,4,5,6,-1]
    #element = 3
    #position = 2

    #Example 2 - test case
    #nums = [70,60,50,-1]
    #element = 40
    #position = 4

    print("element:", element, "position:", position)
    print("original list:", nums)

    for ind in range(len(nums)-1, -1, -1):
        #print("element at index[", ind, "] is : ", nums[ind])
        if ind == len(nums)-1 and nums[ind] != -1:
            print("couldn't find blank position at the end. existing the program")
            break
        else:
            nums[ind] = nums[ind-1]

        if ind == position-1:
            nums[ind] = element
            break

    print("updated list: ",nums)
    return nums

insert_element_at_position([70,60,50,-1],40,4)
