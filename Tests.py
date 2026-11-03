import queue

#should output 0-4 then false once queue is empty
q = queue.queue()
for num in range(5):
    q.appendSong(num)
    print(q.getNextSong())
print(q.getNextSong())

q = queue.queue() #Should output 0-4 in a random order then false
for num in range(5):
    q.appendSong(num)
q.shuffle()
for num in range(6):
    print(q.getNextSong())

q = queue.queue() #add 5 songs play 2 add song next,play the rest
for num in range(5):
    q.appendSong(num)
for num in range(2):
    print(q.getNextSong())
q.addNextSong(9)
for num in range(4):
    print(q.getNextSong())


q = queue.queue() # should play whole queue twice as repeat is enabled
q.enableRepeat()
for num in range(5):
    q.appendSong(num)
for num in range(10):
    print(q.getNextSong())
