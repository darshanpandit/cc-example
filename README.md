##Following is my submission for the Insight Data Engineering Challenge 2015.

###To calculate Feature 1 (WordCount)
This feature requires implementing a global wordcount across all the tweets/documents in the corpus, and then writing the entries into a file sorted alphabetically.
####Implementation
We use Counter, a datastructure abstraction offered in Python to main the global count. We add local counts for each document to update the global counts. Towards the end, we perform an in memory sorting (complexity: nlogn) and write the entries into a file.
####Desired Implementation
In reality, the global-count files may be get really large and might not fit in primary memory. Also, in a distributed system with many workers pushing, the above structure must be highly avaliable.
