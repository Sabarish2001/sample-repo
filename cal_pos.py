def cal_pos(Genome,pattern):
	index_list = []
	t = len(Genome)
	p = len(pattern)
	
	for every_letter in range(t - p  + 1 ):
		if Genome[i : i + p] == pattern:
			index_list.append(i)
	return index_list
	

