sns.distplot(df['friendships_initiated']);
corrmat = df.corr() f, ax =plt.subplots(figsize=(12,9)) sns.heatmap(corrmat, vmax = 0, square=True) plt.show()

sns.set() cols = ['age', 'tenure', 'friend_count', 'www_likes', 'likes_received', 'www_likes_received']

sns.pairplot(df[cols], size = 2.5) plt.show()

G = nx.path_graph(df['age']) pos = nx.draw_circular(G, with_labels = True) nx.draw(G, pos=pos) plt.show()

G = nx.path_graph(df['age']) pos = nx.draw_random(G, with_labels = True) nx.draw(G, pos=pos) plt.show()

G = nx.path_graph(df['age']) pos = nx.draw_spectral(G, with_labels = True) nx.draw(G, pos=pos) plt.show()

G = nx.path_graph(df['age']) pos = nx.draw_spring(G, with_labels = True) nx.draw(G, pos=pos) plt.show()

G = nx.path_graph(df['age']) pos = nx.draw_shell(G, with_labels = True) nx.draw(G, pos=pos) plt.show()
