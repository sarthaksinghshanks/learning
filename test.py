# used_usernames = ["sahil", "rahul_123", "priya22", "aman_ai", "neha"]


# def clean_username(n):
#     list1 = n.split(' ')
#     list2 = []

#     for x in list1:
#         if x != ' ' and x != '':
#             if x.isalpha():
#                 list2.append(x.lower())
#             else:
#                 list2.append(x)

#     name = ''

#     for x in list2:
#         name = name + x

#     return name.strip()


# def check_length(n):

#     stat = True

#     while stat:

#         if len(n) < 5 or len(n) > 15:
#             n = input("Enter username again: ")
#             stat = True
#         else:
#             stat = False

#     return n


# def check_character(n):

#     stat = True

#     while stat:

#         count1 = 0

#         for i in n:

#             if not (i.isalnum() or i == '_'):
#                 count1 = count1 + 1

#         if count1 != 0:
#             n = input("Enter username again: ")
#             stat = True
#         else:
#             stat = False

#     return n


# def check_availability(n):

#     if n in used_usernames:
#         return False
#     else:
#         return True


# name1 = input("Enter name: ")

# name1 = clean_username(name1)

# name1 = check_length(name1)

# name1 = check_character(name1)

# available = check_availability(name1)

# print("Username =", name1)

# if available:
#     print("Status = Username Available")
# else:
#     print("Status = Username Not Available")




# for x in range(1,34):
#     print(x)
#     if x == 12 :
#         break



# list = [1,2,3,4,5]
# print([x+10 for x in list])
# print("hello")

# print([1,2]*12)  


# import seaborn as sns

# print(sns.get_dataset_names())
# penguins = sns.load_dataset('penguins')
# print(penguins)
# sns.set_style('darkgrid')
# sns.scatterplot(data=penguins,x = 'flipper_lenght_mm',y='body_mass_gm',hue='island')



