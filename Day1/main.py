# 1. Write add_numbers(a, b) that returns a + b .

def add_numbers(a,b):
    result= a + b
    return result

print(add_numbers(2,7))

# 2. Write get_even_numbers(numbers: list) -> list using a list comprehension.
numbers=[1,3,4,5,6,77,55,6,4,8]

even_numbers=[x for x in numbers if x % 2==0 ]
print(even_numbers)
# 3. Write count_words(text: str) -> dict that returns a dictionary of word → count.

def count_words(line):
    dict1={}
    words=line.split(" ")
    for word in words:
        if word in dict1:
            dict1[word]= dict1[word] + 1
        else:
            dict1[word]=1   
    return dict1           
print(count_words("apple and banana are my favourite but i like apple more than banana"))



# 4. Write merge_two_dicts(d1: dict, d2: dict) -> dict .

def merge_dict(d1,d2):
    merge = d1|d2
    return merge
print(merge_dict(
    d1={
    'name':'sara',
    'age': 24,
    'gpa':3.0
},
d2={
    'subject':'english',
    'height': 5.8
}))


# 5. Write find_duplicates(items: list) -> list that returns items appearing more than once()

def find_duplicates(user_list):
    list1=[]
    list2=[]
    for item in user_list:
        if item in list1:
            if item not in list2:   # removes duplicates
               list2.append(item)
        else:
            list1.append(item)
    return list2


my_list=([2,8,9,4,6,6,7,3,2,2,9])            
print(find_duplicates(my_list))





