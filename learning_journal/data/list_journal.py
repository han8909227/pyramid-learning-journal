from datetime import datetime


J_1 = 'I learned how to create and use an virtual environment, where scripts from a project can be run in a separate environment (i.e with isolated packages) instead of the bash environment, this is essential to prevent version conflicts on packages.'
J_2 = 'Today I learned how to write a valid test for python functions using pytest, it is surprisingly convenient to use pytest.mark.parametrize to pass in multiple values/lists that we can pass into the testing function.'
J_3 = 'Today we learned how to create our own package via Setuptool, which has it\'s own source code folder and a setup.py file that has references to the author, description and dependencies. I also the importance of breaking the functionalities down to small chunks of codes(functions) and write specific test for each of the chunk, this help paint a much clear picture of errors and it\'s originality.'
J_4 = 'This is day 4 entry'
J_5 = 'Today I worked on several code-war challenges where I familiarized myself with many use case of list compensation, dictionary, tox testing for different py version, and use setup.py to set up my project as a module.'
J_6 = 'Today we learned about TCP/IP and Socket, it is interesting to see the mechanism how data is being generated and transfer through internet (i.e TCP stack model) and also creating our own server with the socket module. (not sure if that\'s the same as an API). Building out the linked-list data structure from scratch definitely helped me understand how array/string multiplication works under the hood and each value is nothing more than an instance of the structure\'s class pointing to a location in memory!'
J_7 = 'Stack is a simple data structure that can be implemented easily, a classic problem to solve the the stack data structure will be the parentheses validator problem (https://www.codewars.com/kata/valid-parentheses/). Using stack we should have O(1) with this problem.'
J_8 = 'Today I learned about Doubly Linked List, where each number does not only have a link to the next number but also a link to the previous number, similar to a queue where you may add a value on the top or bottom'
J_9 = 'Today we learned about the queue, a simple data structure. What makes the queue interesting how it functions: First In First Out, like a waiting in a shopping center the first one to stand in line will get check out first and leave first.'
J_10 = 'This is day 10!'
J_11 = 'Today we learned about the pyramid, a web framework that lays out a back-end architecture for you to utilize and build your website. It reminds me the single page module we were using for JS, Express JS, which has it\'s minimum functionality of routing and establising server, but it seems like frameworks are more comprehensive in terms of architecture and area of uses.'

FMT = '%m/%d/%Y'
Journals = [
    {'id': 1, 'title': 'Day1', 'date': datetime.strptime('10/16/2017', FMT), 'body': J_1},
    {'id': 2, 'title': 'Day2', 'date': datetime.strptime('10/17/2017', FMT), 'body': J_2},
    {'id': 3, 'title': 'Day3', 'date': datetime.strptime('10/19/2017', FMT), 'body': J_3},
    {'id': 4, 'title': 'Day4', 'date': datetime.strptime('10/20/2017', FMT), 'body': J_4},
    {'id': 5, 'title': 'Day5', 'date': datetime.strptime('10/21/2017', FMT), 'body': J_5},
    {'id': 6, 'title': 'Day6', 'date': datetime.strptime('10/23/2017', FMT), 'body': J_6},
    {'id': 7, 'title': 'Day7', 'date': datetime.strptime('10/24/2017', FMT), 'body': J_7},
    {'id': 8, 'title': 'Day8', 'date': datetime.strptime('10/25/2017', FMT), 'body': J_8},
    {'id': 9, 'title': 'Day9', 'date': datetime.strptime('10/26/2017', FMT), 'body': J_9},
    {'id': 10, 'title': 'Day10', 'date': datetime.strptime('10/27/2017', FMT), 'body': J_10},
    {'id': 11, 'title': 'Day11', 'date': datetime.strptime('10/30/2017', FMT), 'body': J_11}

]
