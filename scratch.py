import csv, re

# try:
#     file = open('as.txt', 'r')
#
# except FileNotFoundError:
#     file = open('as.txt', 'w')
#     file.write('adasdf')
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# else:
#     content = file.read()
# finally:
#     raise TypeError("No error")
# fruits = ["Apple", "Pear", "Orange"]
#
#
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
#
# try:
#     make_pie(4)
# except IndexError as error_message:
#     print('fruit pie')
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         total_likes +=0
#
# print(total_likes)

# This opens a text file and converts to csv file, all list items removes the numeric values
with open('fr_50k.txt') as csv_file:
    pattern = r'[0-9]'

    fr_list = [re.sub(pattern, '', line).replace("\n","") for line in csv_file]
    print(fr_list)

with open('fr_50k.csv', 'w') as write_csv:
    csv_writer = csv.writer(write_csv, lineterminator='\n')
    for fr in fr_list:
        csv_writer.writerow([fr])

# for l in fr_list:
#     print(l)
