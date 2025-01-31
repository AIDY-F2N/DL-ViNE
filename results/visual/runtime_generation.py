
import matplotlib.pyplot as plt
import numpy as np

#RUNTIME ******************************************************************************
# Averaged data
algorithms = [ 'NEPA(path)', 'NRPA-DL', 'DL-ViNE']
runtimes = [0.4567615895895636, 0.3574469684108364,  0.2832534573542909] 

fig, ax = plt.subplots(figsize=(8, 4))  

y_pos = np.arange(len(algorithms))

bars = ax.barh(y_pos, runtimes, color='steelblue', edgecolor='black')

ax.set_yticks(y_pos)
ax.set_yticklabels(algorithms, fontsize=12)
ax.invert_yaxis()  

ax.set_xlabel('Runtime per slice (seconds)', fontsize=12)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.02, bar.get_y() + bar.get_height()/2, 
            f'{width:.2f}', va='center', ha='left', fontsize=10)

ax.set_xlim([0, 1])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.show()