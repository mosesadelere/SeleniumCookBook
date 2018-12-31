import shelve

shelfFile = shelve.open('mydata')
bestFriends = ['Aramide', 'Shakirah', 'Qudus', 'Nonso']
shelfFile['bestFriends'] = bestFriends
shelfFile.close()