def find_fibonacci_seq_rec(n):
	if n < 2: return n
	return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)
	


def insertion_sort(seq):
	for i in range(1, len(seq)):
		j = i
		while j > 0 and seq[j-1] > seq[j]:
			seq[j-1], seq[j] = seq[j], seq[j-1]
			j -= 1
	return seq
	
print(insertion_sort([1,4,6,8,3,1,2,100,102,99]))


def selection_sort(seq):
	for i in range(len(seq) -1, 0, -1):
		max_j = i
		for j in range(max_j):
			if seq[j] > seq[max_j]:
				max_j = j
			seq[i], seq[max_j] = seq[max_j], seq[i]
	return seq
	
def gnome_sort(seq):
	i = 0
	while i < len(seq):
		if i ==0 or seq[i-1] <= seq[i]:
			i += 1
		else:
			seq[i], seq[i-1] = seq[i-1], seq[i]
			i -= 1
	return seq
	
def merge_sort(seq):
	if len(seq) < 2:
		return seq
	mid = len(seq)//2
	lft, rgt = seq[:mid], seq[mid:]
	if len(lft)>1:
		lft = merge_sort(lft)
	if len(rgt)>1:
		rgt = merge_sort(rgt)
	
	res = []
	while lft and rgt:
		if lft [-1]>= rgt[-1]:
			res.append(lft.pop())
		else:
			res.append(rgt.pop())
	res.reverse()
	return(lft or rgt) + res
	















