import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('.github/data/action-metrics.csv', parse_dates=['Created At', 'Updated At'])
df = df.rename(columns={'Created At': 'created_at', 'Updated At': 'updated_at', 'Duration (seconds)': 'duration_seconds'})
df['created_at'] = df['created_at'].dt.date
df['updated_at'] = df['updated_at'].dt.date

action_counts = (
    df.groupby(['updated_at', 'Conclusion'])
      .size()
      .unstack('Conclusion', fill_value=0)
      .sort_index()
)

ax = action_counts.plot(kind='bar', stacked=False, figsize=(12, 6))

ax.set_xlabel('Date')
ax.set_ylabel('Number of Actions')
ax.set_title('GitHub Actions by Date and Status')
ax.legend(title='Status')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

for p in ax.patches:
    h = p.get_height()
    if h > 0:
        ax.annotate(
            str(int(h)),
            (p.get_x() + p.get_width() / 2, h),
            ha='center', va='bottom',
            xytext=(0, 3), textcoords='offset points'
        )

plt.savefig('.github/data/action-graph.png', bbox_inches='tight', dpi=150)
plt.close()
