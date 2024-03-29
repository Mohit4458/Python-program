# This is the code of binary search operation


def binary_search(array, target):
    start = 0
    end = len(array)-1
    while start <= end:

        mid = start + ((end - start)//2)

        if array[mid] < target:
            start = mid+1
        elif array[mid] > target:
            end = mid-1
        else:
            return mid

    return -1

def main():
    array = [10, 3, 5, 11, 42, 55]
    target = 3
    ans = binary_search(array, target)
    print(ans)


if _name_ == "_main_":
    main()
