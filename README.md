# Problem Solution
My solution is based on dynamic approach. The solution is nothing like 0/1 Knapsack problem but on different data.
[Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)

Time complexity of this solution is O(n*W) where n is memes amount and W is usb_size in MiB. I'm creating two dimensional table 
that is used for calculating the best current value for given weight and meme value. When algorithm is finished, we have the best
possible value in last column and row of the matrix. Next we need to retrieve our best set of memes, so we start from the end of 
the matrix with best value and check if the best value come from this row, if yes, we push meme name into the set.  
