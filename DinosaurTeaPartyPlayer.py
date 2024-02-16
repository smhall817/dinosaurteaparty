# This file runs the play() function from the file
# DinosaurTeaPartyFunction, with all text output removed.
# To change the number of games played, simply change the
# num_games variable.


from DinosaurTeaPartyFunction import play
import csv
import matplotlib.pyplot as plt
from collections import Counter
from importlib import reload
from matplotlib.ticker import MaxNLocator
plt = reload(plt)


num_games = 100000

data = [("Num Questions", "Chosen Dinosaur", "Questions Asked")]
for i in range(num_games):
    data.append(play())
    
    
with open("DinosaurTeaPartyData.csv", "w") as f:
    csv_writer = csv.writer(f)
    for i in data:
        csv_writer.writerow(i)


zipped_list = list(zip([i[0] for i in data], [i[1] for i in data]))
zipped_list.remove(('Num Questions', 'Chosen Dinosaur'))


turns = [i[0] for i in zipped_list]
dinos = [i[1] for i in zipped_list]
dino_set = list(set(dinos))
dino_set.sort()
labels = Counter(turns).keys()
freq = Counter(turns).values()

fig, (axs1, axs2) = plt.subplots(1, 2, figsize = (20,12), gridspec_kw = {"width_ratios": [1.5, 4]})

axs1.bar(labels, freq, color = 'dodgerblue')
x = [i for i in range(min(labels)-1, max(labels) + 2, 1)]
y = [i for i in range(0, max(freq) + 2, 1)]
axs1.set_xlabel('Number of Questions Asked')
axs1.set_ylabel('Frequency')
axs1.yaxis.set_major_locator(MaxNLocator(integer=True))
axs1.set_title('Number of Questions Required to Reach Answer')

def avg(name, lst):
    count = 0
    total = 0
    for i in reversed(lst):
        if i[1] == name:
            total += i[0]
            lst.remove(i)
            count += 1
    return (name, total/count)

means = []
for i in dino_set:
    means.append(avg(i, zipped_list))
            
axs2.bar([i[0] for i in means], [i[1] for i in means], color = ['green', 'mediumpurple',\
                                'mediumpurple', 'mediumpurple', 'green', 'green', 'mediumpurple',\
                                'mediumpurple', 'mediumpurple', 'green', 'green', 'darkorange',\
                                'darkorange', 'darkorange', 'green', 'green', 'darkorange',\
                                'darkorange', 'darkorange', 'green'])
for tick in axs2.get_xticklabels():
    tick.set_rotation(90)

axs2.set_xlabel('Dinosaur Name')
axs2.set_ylabel('Average Number of Questions Asked')
axs2.set_title('Average Number of Questions Required, By Dinosaur (Bar Color Corresponds to Room Color)')
fig.suptitle(str(num_games) + ' Deductions in "Dinosaur Tea Party"', size=30)
plt.show()



