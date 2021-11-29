#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np


py_df = pd.read_csv('./result/py.txt')
py_df.columns = ['technique', 'datasize', 'time_second']
py_df.sort_values(by=['datasize', 'technique'], inplace=True)
js_df = pd.read_csv('./result/js.txt')
js_df.columns = ['technique', 'datasize', 'time_second']
js_df.sort_values(by=['datasize', 'technique'], inplace=True)


fig, axes = plt.subplots(figsize=(30, 15), nrows=1, ncols=2)

np.random.seed(8)
random_color = ['#' + ''.join([str(x) for x in np.random.choice(list('0123456789ABCDEF'), 6)]) for _ in range(6)]

t_d = {'merge_sort': None, 'quick_sort': None, 'radix_sort': None}

# plot py
i = 0
for tech, df in py_df.groupby('technique'):
	axes[0].plot(df['datasize'], df['time_second'], label=tech, color=random_color[i], alpha=0.8, linewidth=4)
	if tech in t_d.keys():
		t_d[tech] = random_color[i]
	i+=1
axins = inset_axes(axes[0], width="20%", height="20%", loc=3, bbox_to_anchor=(0.77, 0.12, 1, 1), bbox_transform=axes[0].transAxes)
axins.plot(py_df[py_df['technique'] == 'merge_sort']['datasize'], py_df[py_df['technique'] == 'merge_sort']['time_second'], label='merge_sort', color=t_d['merge_sort'], alpha=0.8, linewidth=4)
axins.plot(py_df[py_df['technique'] == 'quick_sort']['datasize'], py_df[py_df['technique'] == 'quick_sort']['time_second'], label='quick_sort', color=t_d['quick_sort'], alpha=0.8, linewidth=4)
axins.set_xlabel('Size (n)', fontweight='bold')
axins.set_ylabel('Seconds (s)', fontweight='bold')
axes[0].set_xlabel('Size (n)', fontweight='bold')
axes[0].set_ylabel('Seconds (s)', fontweight='bold')
axes[0].set_ylim(0, 300)
axes[0].legend()
axes[0].set_title('Python Sort Running Time')

# plot js
i = 0
for tech, df in js_df.groupby('technique'):
	axes[1].plot(df['datasize'], df['time_second'], label=tech, color=random_color[i], alpha=0.8, linewidth=4)
	if tech in t_d.keys():
		t_d[tech] = random_color[i]
	i+=1
axins = inset_axes(axes[1], width="20%", height="20%", loc=3, bbox_to_anchor=(0.77, 0.32, 1, 1), bbox_transform=axes[1].transAxes)
axins.plot(js_df[js_df['technique'] == 'merge_sort']['datasize'], js_df[js_df['technique'] == 'merge_sort']['time_second'], label='merge_sort', color=t_d['merge_sort'], alpha=0.8, linewidth=4)
axins.plot(js_df[js_df['technique'] == 'quick_sort']['datasize'], js_df[js_df['technique'] == 'quick_sort']['time_second'], label='quick_sort', color=t_d['quick_sort'], alpha=0.8, linewidth=4)
axins.plot(js_df[js_df['technique'] == 'radix_sort']['datasize'], js_df[js_df['technique'] == 'radix_sort']['time_second'], label='radix_sort', color=t_d['radix_sort'], alpha=0.8, linewidth=4)
axins.set_xlabel('Size (n)', fontweight='bold')
axins.set_ylabel('Seconds (s)', fontweight='bold')
axes[1].set_xlabel('Size (n)', fontweight='bold')
axes[1].set_ylabel('Seconds (s)', fontweight='bold')
axes[1].set_ylim(0, 10)
axes[1].legend()
axes[1].set_title('Javascript Sort Running Time')


plt.show()