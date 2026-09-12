import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	dotproc=0
	z1=0
	z2=0
	l2v1=0
	l2v2=0
	if v1.size==0 or v2.size==0 or len(v1)!=len(v2) :
		return -1
	for i in range(len(v1)):
		dotproc+=v1[i]*v2[i]
		if z1==0:
			z1+=1
		if z2==0:
			z2+=1
		l2v1+=v1[i]*v1[i]
		l2v2+=v2[i]*v2[i]
	if z1==v1.size or z2==v2.size:
		return -1
	l2v1=l2v1**0.5
	l2v2=l2v2**0.5
	return dotproc/(l2v1*l2v2)
	pass