#input 1: sequence length n
#input 2: a = value sequence
#input constraints = (2 <= n) and (n <= (2 * (10 ** 5))) 
# constraint2 = v[i] >= 0 and (v[i] <= 2 * (10 ** 5) )


n = int(input())
#a is a sequence defined by looping through the split (by spaces) input, where each is typed as int
a = [int(x) for x in input().split()]


#NOTES
#i and j are used as temp variables to represent index positions ( because you need to loop through sequence a by index)
#i range = 0 , ... , n-1
#j range = 1 , ... , n-1
# I think this difference in range ensures that i != j 
#max() returns the maximum value: var product or the product of a[i] * a[j]

#SLOW SOLN

#product = 0
# for i in range(n):
#    for j in range(i + 1, n):
#        product = max(product, a[i] * a[j])
# print(product)

# this solution is slow for large sequences as n ** 2 operations are performed to fint the max product
#break it down to just find the largest integers and their product will be the max product

#FAST SOLN
index1 = 1
for i from 2 to n:
    if a[i] > a[index1]:
        index1 = i

index2 = 1
# for i from 2 to n:
#     if a[]