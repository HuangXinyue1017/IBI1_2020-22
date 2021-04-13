seq='agctTgaCgtAagtgg'
# Answer: TCGAACTGCATTCACC

def reverse_complement_calculator(s):
	dict={'A':'T','G':'C','C':'G','T':'A'}
	s=s.upper()
	new_s=''
	for i in range(0,len(s)):
		new_s+=dict[s[i]]
	new_s=new_s[::-1]
	return new_s

print(reverse_complement_calculator(seq))