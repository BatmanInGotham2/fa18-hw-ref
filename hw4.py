"""
CS 196 FA18 HW4
Prepared by Andrew, Emilio, and Prithvi

You might find certain default Python packages immensely helpful.
"""

# Good luck!

"""
most_common_char

Given an input string s, return the most common character in s.
"""
def most_common_char(s):
	if s == None or len(s) == 0:
		return None
	dict = {}
	for c in s:
		if c in dict:
			dict[c] = dict[c] + 1
		else:
			dict[c] = 1
	return max(dict, key=dict.get)

#print(most_common_char("bcds"))

"""
alphabet_finder

Given an input string s, return the shortest prefix of s (i.e. some s' = s[0:i] for some 0 < i <= n)
that contains all the letters of the alphabet.
If there is no such prefix, return None.
Your function should recognize letters in both cases, i.e. "qwertyuiopASDFGHJKLzxcvbnm" is a valid alphabet.

Example 1:
	Argument:
		"qwertyuiopASDFGHJKLzxcvbnm insensitive paella"
	Return:
		"qwertyuiopASDFGHJKLzxcvbnm"

Example 2:
	Argument:
		"aardvarks are cool!"
	Return:
		None
"""
def alphabet_finder(s):
	if s == None or len(s) == 0:
		return None
	alpha = "abcdefghijklmnopqrstuvwxyz"
	str = s.lower()
	strs = []
	for i in range(0, len(s)):
		alpha = "abcdefghijklmnopqrstuvwxyz"
		count = i
		while len(alpha) > 0 and count < len(str):
			if str[count] in alpha:
				alpha = alpha.replace(str[count], "")
			count += 1
		if len(alpha) == 0:
			strs.append(s[i:count])
	if(len(strs) == 0):
		return None
	mini = 0
	minL = len(strs[0])
	for i in range(0, len(strs)):
		if(len(strs[i]) < minL):
			mini = i
			minL = len(strs[i])
	return strs[mini]

#print(alphabet_finder("abcdefghxcvbnm insensitive paella"))

"""
longest_unique_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that arr[a:a+b] is the longest unique subarray.
That is to say, all the elements of arr[a:a+b] must be unique,
and b must be the largest value possible for the array.
If multiple such subarrays exist (i.e. same b, different a), use the lowest value of a.

Example:
	Argument:
		[1, 2, 3, 1, 4, 5, 6]
	Return:
		[1, 6]
"""
def longest_unique_subarray(arr):
	lists = []
	if arr is None or len(arr) == 0:
		return None
	for i in range(0, len(arr)):
		sublist = []
		valueList = []
		count = i
		while count < len(arr) and arr[count] not in valueList:
			sublist.append(count)
			valueList.append(arr[count])
			count += 1
		lists.append(sublist)
	if len(lists) == 0:
		return None
	returnList = []
	returnList.append((max(lists, key=len))[0])
	returnList.append(len(max(lists, key=len)))
	return returnList

#print(longest_unique_subarray([1,2,1]))

"""
string_my_one_true_love

A former(?) CA for this course really like[d] strings that have the same occurrences of letters.
This means the staff member likes "aabbcc", "ccddee", "abcabcabc", etcetera.

But the person who wrote all of your homework sets wants to trick the staff with really long strings,
that either could be the type of string that the staff member likes,
or a string that the CA would like if you remove exactly one character from the string.

Return True if it's a string that the homework creator made, and False otherwise.
Don't treat any characters specially, i.e. 'a' and 'A' are different characters.

Ungraded food for thought:
Ideally, your method should also work on integer arrays without any modification.

Example 1:
	Argument:
		"abcbabcdcdda"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
	Return:
		True

Example 2:
	Argument:
		"aaabbbcccddde"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. We have 1 e, which we can remove.
	Return:
		True

Example 3:
	Argument:
		"aaabbbcccdddeeffgg"
		This string is similar to the other ones, except with 2 e's, f's and g's at the end.
		To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
		one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
	Return:
		False
"""
def string_my_one_true_love(s):
	if s == None or len(s) == 0:
		return False
	if len(s) == 1:
		return True
	dict = {}
	for c in s:
		if c in dict:
			dict[c] = dict[c] + 1
		else:
			dict[c] = 1
	minim = min(dict, key=dict.get)
	maxim = max(dict, key=dict.get)
	check = 0
	if dict[maxim] != dict[minim]:
		listOfKeys = []
		for item in dict:
			if dict[item] == dict[minim]:
				listOfKeys.append(item)
		if len(listOfKeys) > 1:
			check = dict[maxim] - 1
			dict[maxim] = dict[maxim] - 1
		else:
			check = dict[maxim]
			dict[minim] = dict[minim] - 1

		for d in dict:
			if dict[d] != check and dict[d] != 0:
				return False
	return True

#print(string_my_one_true_love("abcbabcdcdda"))

"""
alive_people

You are given a 2-dimensional list data. Each element in data is a list [birth_year, age_of_death].
Assume that the person was alive in the year (birth_year + age_of_death).
Given that data, return the year where the most people represented in the list were alive.
If there are multiple such years, return the earliest year.

Example:
	Argument:
		[[1920, 80], [1940, 22], [1961, 10]]
	Return:
		1961
"""
def alive_people(data):
	if data is None or len(data) == 0:
		return None
	dict = {}
	for i in data:
		for j in range(0, i[1] + 1):
			year = i[0] + j
			if year in dict:
				dict[year] = dict[year] + 1
			else:
				dict[year] = 1
	maxim = max(dict, key=dict.get)
	list = []
	for d in dict:
		if dict[d] == dict[maxim]:
			list.append(d)
	return min(list)

#print(alive_people([[1920, 80], [1940, 22], [1961, 10]]))

"""
three_sum

Given an input list of integers arr, and a constant target t,
is there a triplet of distinct elements [a,b,c] so that a + b + c = t?

Return a 2-dimensional list of all the unique triplets as defined above.
Each inner list should be a triplet as we defined above.
We don't care about the order of triplets, nor the order of elements in each triplet.

Example:
	Arguments:
		[-1, 0, 1, 2, -1, -4], 0
	Return:
		[
			[-1, 0, 1],
			[-1, -1, 2]
		]
"""
def three_sum(arr, t):
	pass


"""
happy_numbers

Given an input integer n > 0, return the number of happy integers between 1 and n, bounds inclusive.
https://en.wikipedia.org/wiki/Happy_number

Example 1:
	Argument:
		8
		The happy numbers between 1 and 8 are 1 and 7 (7 -> 49 -> 97 -> 130 -> 10 -> 1)
	Return:
		2468 // 1234 (i.e., 2)
Example 2:
	Argument:
		15
	Return:
		4294967296 ** (1 / 16) (i.e., 4)
"""
def happy_numbers(n):
	pass







"""
zero_sum_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that sum(arr[a:a+b]) == 0.
In plain English, give us the location of a subarray of arr that starts at index a
and continues for b elements, so that the sum of the subarray you indicated is zero.
If multiple such subarrays exist, use the lowest valid a, and then lowest valid b,
in that order of priority.
If no such subarray exists, return None.

Ungraded food for thought:
Think about how to generalize your solution to any arbitrary target sum.

Example 1:
	Argument:
		[0, 1, 2, 3, 4, 5]
		Clearly, the first element by itself forms a subarray with sum == 0.
	Return:
		[0, 1]

Example 2:
	Argument:
		[10, 20, -20, 3, 21, 2, -6]
		In this case, arr[1:3] = [20, -20], so there is a zero sum subarray.
	Return:
		[1, 2]
"""
def zero_sum_subarray(arr):
	lists = []
	if arr is None or len(arr) == 0:
		return None
	for i in range(0, len(arr)):
		count = i + 1
		sum = arr[i]
		sublist = []
		sublist.append(i)
		while count < len(arr) and sum != 0:
			sum += arr[count]
			sublist.append(count)
			count += 1
		if sum == 0:
			lists.append(sublist)
	if len(lists) == 0:
		return None
	returnList = []
	returnList.append((min(lists, key=len))[0])
	returnList.append(len(min(lists, key=len)))
	return returnList

#print(zero_sum_subarray([1, 1, 2, 3, -5]))
