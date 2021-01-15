import array
import collections
d = collections.OrderedDict(key1=1, key2=2, key3=3)
# creating an ordered dictionary to reference later
print(d)

d["key4"] = 4  # this adds another key and value to dictionary

print(d.keys())  # prints all current keys

print(d.values())  # prints all current values

d["key5"] = 5  # creating a key and value after the print results
# in no return.

# Arrays
arr = array.array("f", (1.0, 2.0, 3.0, 4.0, 5.0))  # 'f' means the array
# will expect a float value.
print(arr)

del arr[1]  # deletes the second item in array 1.0 = 0,  2.0 = 1

print(arr)

arr.append(16.0)  # append adds the float to the end of the array

print(arr)
