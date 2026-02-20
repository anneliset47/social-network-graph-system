#!/usr/bin/env python
# coding: utf-8

# #Question 1 (30 points): Designing a System

# You are tasked with designing a system to manage a large dataset of social media connections. The dataset comprises billions of users and their connections (friendship links) in a social network. Each user has an ID and maintains a list of their friends' IDs. Every user has defined hobbies, music, and movie preferences.
#
# **Design an efficient system that:**
#
# 1. Store and manage this dataset considering the massive scale.
# 2. Allows for quick retrieval of a user's friends or the friends of friends up to a certain level.
# 3. Implements algorithms to suggest new friends to a user based on mutual friends or other relevant criteria (preferences of Hobbies, Music/Movies).
# 4. Optimizes for space and time complexities in operations like adding new users, adding connections, and suggesting new connections.
# 5. Define a name and a description for the classes and functions/methods you will implement. Add this list to your report.
#
# **Your solution should include:**(must be included in your report)
#
# 1. A mind map with images and text for your approach encourages creativity and imagination in presentation. (take some ideas about mind maps here: https://mindmapsunleashed.com/10-really-cool-mind-mapping-examples-you-will-learn-fromLinks to an external site.).
# 2. A general approach to your solution (4-5 paragraphs)
# 3. A detailed explanation of the data structures you would use to store the user data and their connections, considering the scale of the dataset.
# 4. Algorithms for efficiently retrieving friends or friends of friends within a limited degree of separation.
# 5. Strategies for suggesting new connections to users.
# 6. Analysis of the time and space complexities of your proposed solution, highlighting its efficiency and scalability.
#
# **Code/Jupyter Notebook:**
#
# A Python code with a small dataset including users (with hobbies/music/movie preferences), their friends, and a recommendation working algorithm.
#
# **Additional Notes:**
#
# * Consider scenarios where the dataset continues to increase.
# * Discuss any trade-offs, limitations, or challenges your proposed system might encounter.
# * Please ensure that you include any rational assumptions in your report.
# * Create one comprehensive Jupyter Notebook with the report and your working code.
# * If you need to upload any additional files with code, such as CSV, txt, jpg, or any other important files, please submit them to Canvas. Please make sure that you compile your solution with the uploaded files.
#
# **Grading:**
#
# * 15 points for the details of explanations/descriptions, algorithms used, and their complexity (Space and Time), classes, and methods (names and tasks).
# * 15 for the running Code in Python. (Jupyter Notebook)
# This question encompasses multiple aspects of data structures (like graphs, trees, hash maps), algorithms (graph traversal, recommendation algorithms), and problem-solving strategies (optimization, scalability). It challenges you to apply your understanding of these concepts and think critically about designing a system that addresses real-world issues at a large scale.

# In[ ]:


from collections import deque
import random

#adjacency list to represent friendship connections
graph = {
    "user_id1": {"user_id2": 1, "user_id3": 1, "user_id4": 1},
    "user_id2": {"user_id1": 1, "user_id3": 1, "user_id5": 1, "user_id9": 1},
    "user_id3": {"user_id1": 1, "user_id2": 1, "user_id6": 1, "user_id8": 1, "user_id9": 1},
    "user_id4": {"user_id1": 1, "user_id5": 1, "user_id8": 1, "user_id9": 1},
    "user_id5": {"user_id4": 1, "user_id9": 1},
    "user_id6": {"user_id3": 1, "user_id7": 1, "user_id9": 1},
    "user_id7": {"user_id6": 1, "user_id8": 1, "user_id9": 1},
    "user_id8": {"user_id3": 1, "user_id4": 1, "user_id7": 1, "user_id9": 1},
    "user_id9": {"user_id2": 1, "user_id3": 1, "user_id4": 1, "user_id5": 1, "user_id6": 1, "user_id7": 1, "user_id8": 1, "user_id10": 1},
    "user_id10": {"user_id9": 1}
}

#hash maps to store users' hobbies, music, and movies preferences
hobby_dictionary = {"user_id1": "hiking",
                     "user_id2": "running",
                     "user_id3": "skiing",
                     "user_id4": "climbing",
                     "user_id5": "skiing",
                     "user_id6": "climbing",
                     "user_id7": "hiking",
                     "user_id8": "hiking",
                     "user_id9": "skiing",
                     "user_id10": "running"
}

music_dictionary = {"user_id1": "pop",
                    "user_id2": "pop",
                    "user_id3": "country",
                    "user_id4": "alternative",
                    "user_id5": "rock",
                    "user_id6": "pop",
                    "user_id7": "rock",
                    "user_id8": "country",
                    "user_id9": "pop",
                    "user_id10": "rock"
}

movie_dictionary = {"user_id1": "comedy",
                    "user_id2": "drama",
                    "user_id3": "comedy",
                    "user_id4": "sci-fi",
                    "user_id5": "sci-fi",
                    "user_id6": "drama",
                    "user_id7": "drama",
                    "user_id8": "comedy",
                    "user_id9": "sci-fi",
                    "user_id10": "comedy"
}

class Graph:
    def __init__(self, graph: dict = {}, hobbies=None, music=None, movies=None):
        #initialize the graph and preferences
        self.graph = graph
        self.hobbies = hobbies
        self.music = music
        self.movies = movies

    def first_degree_connections(self, user_id):
        #return keys of inner dictionary in graph
        return list(self.graph.get(user_id, {}).keys())

    def second_degree_connections(self, user_id):
        #store unique second degree connections
        second_degree_connections = set()
        #store unique visited users
        visited = set()
        queue = deque([(user_id, 0)]) #depth 0

        while queue:
            #get the next user and depth from the queue
            current_user, depth = queue.popleft()

            #stop at second-degree connections
            if depth > 1:
                continue

            if current_user not in visited:
                #mark the user as visited
                visited.add(current_user)

                #loop through current user's friends
                for friend in self.graph.get(current_user, {}):
                    if friend not in visited:
                        if depth == 1:
                            second_degree_connections.add(friend)
                        #add the friend to the queue with increased depth
                        queue.append((friend, depth + 1))

        return second_degree_connections

    def third_degree_connections(self, user_id):
        third_degree_connections = set()
        visited = set()
        queue = deque([(user_id, 0)]) #depth 0

        while queue:
            #get the next user and depth from the queue
            current_user, depth = queue.popleft()

            #stop at third-degree connections
            if depth > 2:
                continue

            if current_user not in visited:
                #mark the user as visited
                visited.add(current_user)

                #loop through current user's friends
                for friend in self.graph.get(current_user, {}):
                    if friend not in visited:
                        if depth == 2:
                            third_degree_connections.add(friend)
                        #add the friend to the queue with increased depth
                        queue.append((friend, depth + 1))

        return third_degree_connections

    def suggest_connections_based_on_interests(self):
        suggested_graph = {}

        #loop through each user
        for user in self.graph.keys():
            #initialize suggestions for the user
            suggested_graph[user] = {}

            #compare with every other user
            for potential_friend in self.graph.keys():
                if user == potential_friend or potential_friend in self.graph[user]:
                    #skip self and already connected friends
                    continue

                #calculate similarity score based on interests
                similarity_score = 0
                if self.hobbies.get(user) == self.hobbies.get(potential_friend):
                    similarity_score += 1
                if self.music.get(user) == self.music.get(potential_friend):
                    similarity_score += 1
                if self.movies.get(user) == self.movies.get(potential_friend):
                    similarity_score += 1

                #only suggest if there is some similarity
                if similarity_score > 0:
                    suggested_graph[user][potential_friend] = similarity_score

        return suggested_graph

#create graph instances
G = Graph(graph=graph, hobbies=hobby_dictionary, music=music_dictionary, movies=movie_dictionary)

#test code:
print("First degree connections:", G.first_degree_connections("user_id10"))
print("Second degree connections:", G.second_degree_connections("user_id10"))
print("Third degree connections:", G.third_degree_connections("user_id10"))

suggested_graph = G.suggest_connections_based_on_interests()
print("\nSuggested Connections:")
for user, suggestions in suggested_graph.items():
    print(f"{user}: {suggestions}")


# #Question 2 (25 points): Divide and Conquer Algorithm

# In this question, you will implement a Divide and Conquer algorithm for finding the maximum subarray sum (also known as Kadane's Algorithm) and compare it with a brute-force solution.
#
#
#
# **2.1) Implement both solutions and compare/analyze their time complexity.**
#
# > **A. Brute Force Approach: (10 points)**
#
# > Given an array of integers, A = [-2, 1, -3, 4, -1, 2, 1, -5, 4], find the  maximum sum of any contiguous subarray using the brute-force approach.
#
# > Describe the algorithm and show all steps to arrive at the correct result.

# In[ ]:


A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def brute_force(array):
  max_sum = array[0]
  #iterate over each element in the array to set the starting point of a subarray
  for i in range(len(A)):
    #iterate from the current starting point to the end of the array to form subarrays
    for j in range(i, len(A)):
      #calculate the sum of the current subarray from index i to j
      curr = sum(A[i:j+1])
      #update max_sum if the current subarray sum (curr) is greater than the previous max_sum
      max_sum = max(max_sum, curr)
  return max_sum

print(brute_force(A))


# Description of Algorithm:
#
# This algorithm iterates through all possible subarrays, calculating the sum of each subarray, and updating the max_sum whenever a higher sum is found. The time complexity is O(n^3).

# > **B. Divide and Conquer Approach: (10 points)**
#
# > Implement the Divide and Conquer approach to solve the Maximum Subarray Problem. Your solution should divide the array into two halves and recursively compute the maximum subarray sum in each half, as well as the maximum sum that crosses the middle.

# In[ ]:


def divide_and_conquer(array, start, end):
  #base case: if the subarray has only one element
  if start == end:
    #max sum is the single element itself
    return array[start]

  #calculate the midpoint
  mid = (start + end) // 2
  #recursively find the max subarray sum of the left half
  left_max = divide_and_conquer(array, start, mid)
  # recursively find the max subarray sum of the right half
  right_max = divide_and_conquer(array, mid + 1, end)
  #find the max sum that crosses the midpoint
  cross_max = find_cross_max(array, start, mid, end)
  #return the maximum of the three cases
  return max(left_max, right_max, cross_max)

def find_cross_max(array, start, mid, end):
  #initialize left_sum and right_sum to negative infinity
  left_sum = float('-inf')
  right_sum = float('-inf')
  for i in range(mid, start - 1, -1):
    #calculate the sum of the left half
    left_sum = max(left_sum, sum(array[i:mid+1]))
  for j in range(mid + 1, end + 1):
    #calculate the sum of the right half
    right_sum = max(right_sum, sum(array[mid+1:j+1]))
  #combine results
  return left_sum + right_sum

divide_and_conquer(A, 0, len(A)-1)


# Description of Algorithm:
#
# This algorithm uses dynamic programming to recursively divide the array into smaller arrays, solve for the left and right halves, and the subarray that spans the midpoint. It then calculates the max_sum of seach of these and returns the highest value. The time complexity is O(n^2).

# **2.2) Modify your Divide and Conquer algorithm (5 points)**
#
# Modify your Divide and Conquer algorithm to handle an additional constraint: Find the maximum subarray that must include a particular index i (where i is given as an input).
#
# Explain how the algorithm works with this new constraint and discuss the time complexity of the modified solution.

# In[ ]:


index_oi = int(input("Enter the index of interest: "))

def divide_and_conquer(array, start, end, index_oi):
  #base case: if the subarray has only one element
  if start == end:
    #ensure subarray includes index of interest
    if start == index_oi:
      return array[start]
    else:
      return float('-inf')

  #check index of index is within current range
  if index_oi < start or index_oi > end:
    #exclude subarrays that don't include index of interest
    return float('-inf')

  #calculate the midpoint
  mid = (start + end) // 2
  #recursively find the max subarray sum of the left half
  left_max = divide_and_conquer(array, start, mid, index_oi)
  # recursively find the max subarray sum of the right half
  right_max = divide_and_conquer(array, mid + 1, end, index_oi)
  #find the max sum that crosses the midpoint
  cross_max = find_cross_max(array, start, mid, end)
  #return the maximum of the three cases
  return max(left_max, right_max, cross_max)

def find_cross_max(array, start, mid, end):
  #initialize left_sum and right_sum to negative infinity
  left_sum = float('-inf')
  right_sum = float('-inf')
  for i in range(mid, start - 1, -1):
    #calculate the sum of the left half
    left_sum = max(left_sum, sum(array[i:mid+1]))
  for j in range(mid + 1, end + 1):
    #calculate the sum of the right half
    right_sum = max(right_sum, sum(array[mid+1:j+1]))
  #combine results
  return left_sum + right_sum

divide_and_conquer(A, 0, len(A)-1, index_oi)


# Description of Algorithm:
#
# This algorithm finds the max_sum of a subarray that includes a specific index of interest by recursively dividng the array into smaller subarrays, ensuring that the subarray being considered always includes the index of interest, and then calculates the max_sum of the left, right, and crossing subarrays. The time complexity is O(n*logn).
#

# #Question 3 (25 points): Dynamic Document Search Engine

# **Scenario:**
#
# Imagine you are building the backend for a document search engine that allows users to search for specific terms in a set of documents. The system must be optimized for speed and memory efficiency, as it will need to handle millions of documents.
#
# **3.1 Document Representation: (10 points)**
#
# > Each document contains a set of words. A word can appear multiple times in a document.
#
# > Create a data structure that allows you to efficiently store documents, where a unique ID identifies each document, and each word is stored along with its frequency in the document.

# In[ ]:


#example data structure- outer dictionary for document IDs and inner dictionary where key=word from document and value=word frequency
documents = {
    "doc1":{"word1":10, "word2":15, "word3":20},
    "doc2":{"word1":10, "word2":15, "word3":20},
    "doc3":{"word1":10, "word2":15, "word3":20},
    "doc4":{"word1":15, "word2":20,}
}


# **3.2 Search Functionality: (10 points)**
#
# > Implement a search function that can quickly return the documents that contain a given word. Additionally, return the frequency of the word within each document.

# In[ ]:


def search(word):
  #initialize results dictionary to store document IDs and word frequencies
  results = {}
  #loop through each document in the 'documents' dictionary
  for doc_id, doc in documents.items():
    #check if the word of interest is in the doc
    if word in doc:
      #if found in the doc, add the doc ID as a key and the frequency of the word as the value in the results dict
      results[doc_id] = doc[word]
  return results

search("word1")


# **3.3 Advanced Query Support: (5 points)**
#
# > Implement support for AND and OR queries, where users can search for documents containing multiple words.
#
#
#
# For example:
#
# > "apple AND banana" should return documents containing both "apple" and "banana".
#
# > "apple OR banana" should return documents containing either "apple" or "banana".
#
#
# **Hints:**
#
# * Efficiency Considerations: Consider breaking down the problem into two parts: storing the data and querying it.
# * Edge Cases: What happens if a word does not appear in any document? What if you query for words with typos or partial matches?

# In[ ]:


def and_search(word1, word2):
  #initialize results dictionary to store document IDs and word frequencies
  results = {}
  #loop through each document in the 'documents' dictionary
  for doc_id, doc in documents.items():
    #if both words are in the doc
    if word1 in doc and word2 in doc:
      #sum their frequencies
      results[doc_id] = doc[word1] + doc[word2]
  return results

def or_search(word1, word2):
  #initialize results dictionary to store document IDs and word frequencies
  results = {}
  #loop through each document in the 'documents' dictionary
  for doc_id, doc in documents.items():
    #if at least one of the words is in the doc
    if word1 in doc or word2 in doc:
      #sum their frequencies
      results[doc_id] = doc.get(word1, 0) + doc.get(word2, 0)
  return results

print("AND:", and_search("word2", "word3"))
print("OR:", or_search("word2", "word3"))
