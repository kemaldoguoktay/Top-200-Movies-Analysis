import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_excel('Top_200_Movies.xlsx')

movies = np.array(movies)

title = movies[:5,1]
money = movies[:5,3]

fig = plt.figure()
plt.pie(money, labels=title, autopct='%1.1f%%', textprops={'fontsize': 8})
plt.title('What are the Earning Rates of the 5 Movies\nwith the Highest Box Office Earnings in 2023?\n' , size = 15, fontweight='bold', color='blue')
plt.figtext(0.3, 0.01, '\n\nSuper Mario    = The Super Mario Bros. Movie\nSpider-Man     = Spider-Man: Across the Spider-Verse\nAvatar             = Avatar: The Way of Water\nBlack Panther = Black Panther: Wakanda Forever ', ha='left', fontsize=8)
plt.figtext(0.05, -0.17, "This piechart graph shows the results of the earning rates of the 5 movies with the highest box office earnings in 2023.\nFrom the pie chart, it is clear that Avatar: The Way of Water has the highest box office earning.\nMoreover, the earnings of Super Mario and Barbie is close to be most financially successful.")
plt.show()

df = pd.DataFrame(movies)
Warners_mean = np.mean(df[df[5] == 'Warner Bros.'][3])
Century_mean = np.mean(df[df[5] == '20th Century Studios'][3])
Universal_mean = np.mean(df[df[5] == 'Universal Pictures'][3])
Disney_mean = np.mean(df[df[5] == 'Walt Disney Studios Motion Pictures'][3])
Columbia_mean = np.mean(df[df[5] == 'Columbia Pictures'][3])

Distributor = np.array([Warners_mean,Century_mean,Universal_mean,Disney_mean,Columbia_mean])
Dist_title = "Warners","Century","Universal","Disney","Columbia"
print("\n")
fig = plt.figure()
plt.pie(Distributor, labels=Dist_title, autopct='%1.1f%%', textprops={'fontsize': 8})
plt.title('What is the average earnings of distributors\n according to their movies in the top 200', size = 15, fontweight='bold', color='blue')
plt.figtext(0.3, 0.01, '\n\nWarners    = Warner Bros. \nCentury     = 20th Century Studios\nUniversal   = Universal Pictures\nDisney       = Walt Disney Studios Motion Pictures ', ha='left', fontsize=8)
plt.figtext(0.05, -0.20, "This piechart graph shows the results of the rate of the mean of the earnings in the 5 distributors with the highest box office \nearnings in 2023.From the pie chart, it is clear that 20th Century Studios has an epic results, they do not present a \nless profitable movie. In the graph, we can interpret that 20th Century Studios allocated most of her focus to this movie, and \nthey seem very successful. On the contrary, Warner Bros. present a lot of movie in top 200 list, and they have a movie \nwhich is in the top 2 of the list; however, their success rate is very low compared to other distributors. ")
plt.show()
