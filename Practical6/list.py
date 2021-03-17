import matplotlib.pyplot as plt
import numpy as np

# A dictionary about genes
genes_lengths = [9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]

#Calculate the total length of genes
tot_len = 0
for i in range(len(genes_lengths)):
	tot_len += genes_lengths[i]

#Calculate the total numbers of exons
tot_exon = 0
for i in range(len(exon_counts)):
	tot_exon += exon_counts[i]

#Calculate the average
a = np.array(genes_lengths)
b = np.array(exon_counts)
c = a/b

#Sort the array and print
c.sort()
print('Average exon length:', c)

#Make the boxplot
plt.boxplot(c)

plt.xticks([1], ['Average exon length'])
plt.ylabel('Distribution')
plt.title('The boxplot')

plt.grid(axis="y", ls=":", lw=1, color="grey", alpha=0.4)

plt.show()