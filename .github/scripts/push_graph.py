import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('.github/data/push-metrics.csv', parse_dates=['Date'])
df['day'] = df['Date'].dt.date
daily = df.groupby('day').size()

ax = daily.plot(kind='bar', figsize=(12,6))
ax.set_title('Pushes to main per dag')
ax.set_xlabel('Dato')
ax.set_ylabel('Antal pushes')
for p in ax.patches:
    h = p.get_height()
    if h>0:
        ax.annotate(str(int(h)), (p.get_x()+p.get_width()/2, h), ha='center', va='bottom', xytext=(0,3), textcoords='offset points')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('.github/data/push-graph.png', dpi=150, bbox_inches='tight')
plt.close()
