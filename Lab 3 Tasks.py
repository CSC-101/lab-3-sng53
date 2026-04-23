#Task 1
more = [x + 1 for x in [1,2,3,4]]   #List, in order, the values that x takes at each step. Step 1: x = 1, Step 2: x = 2, Step 3: x = 3, Step 4: x = 4
print ()                            # What is the value of more at this point? The value of more at this point is [2,3,4,5]


def square (n:int) -> int:
    return n * n                    # Record, in order of the calls, each value of n and the corresponding return value.
                                    # Step 1: n = 1 return value = 1, Step 2: n = 2 return value = 4, Step 3: n = 3 return value = 9, Step 4: n = 4 return value = 16
squares = [square(x) for x in [1,2,3,4]]    # What is the value of squares and how does this relate to the values recorded above? The value of square is [1,4,9,16]. This relates to the values recorded above because squares is [1,4,9,16] which matches the return values of sqaure (n) for each input in order.
print ()


def check(n: int) -> bool:
    return n > 2                    # Record, in order of the calls, each value of n and the corresponding return value
                                    # Step 1: n = 0 return value = False, Step 2: n = 1 return value = False, Step 3: n = 2 return value = False
                                    # Step 4: n = 3 return value = True, Step 5: n = 4 return value = True
answer = [x for x in range(5) if check(x)]  # What is the value of answer? The value of answer is [3,4]
print ()


def inc(m: int) -> int:
    return m + 1                    # Record, in order of the calls, each value of m and the corresponding return value
                                    # m = 3 return value = 4, m = 4 return value = 5
def check(n:int) -> bool:
    return n > 2                    # Record, in order of the calls, each value of n and the corresponding return value.
                                    # n = 0 return value = False, n = 1 return value = False, n = 2 return value = False, n = 3 return value = True
answer = [inc(x) for x in range(5) if check(x)]     # What is the value of answer? The value of answer is [4,5]
print ()


# Task 2
def tally (nums: list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num         # Record each value of total and num at the end of the loop body
                                    # 1. total = 4, num = 4 2.total = 13, num = 9 3. total = 15, num = 2 4. total = 16, num = 1
    return total

result = tally([4,9,2,1])


def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])  # Record each value of new_list and idx at the end of t
                                    # 1. new_list = [4], idx = 0 2. new_list = [4,9], idx = 1 3. new_list = [4,9,2], idx = 2 4. new_list = [4,9,2,1], idx = 3
    return new_list             # How does this loop differ from that above? The first loop goes through the list and combines all the numbers into one total. While this loop goes through the list and bulids a new list with the same elements

result = copy([4,9,2,1])


def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)      # Record each value of new_list and value at the end of the loop body
    return new_list                     # 1. new_list = [5], value = 4 2. new_list = [5,10], value = 9 3. new_list = [5,10,3], value = 2 4. new_list = [5,10,3,2], value = 1

result = increment_all([4,9,2,1])

