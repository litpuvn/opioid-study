#  Visualization the interaction between users in a subreddit from Reddit.com.

##  Input: a json file downloaded from Reddit.com
##  Output: a matrix representing the interaction between users.
###   a).If a user posts a topic and no one replies, there is no edge;
###   b).If a post is commented by a user and the author of the post commented back, there will be an edge;
