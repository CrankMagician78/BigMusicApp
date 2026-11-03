import random
#queue needs to support adding items to the beginning and as the next song, inserting items at any given position and moving songs
class queueItem():
    def __init__(self,songData):
        self.song = songData
    def output(self):
        print(self.song)

class queue():
    def __init__(self):
        self._queue = []
        self._playerHead = -1
        self._queueLength = 0
        self._remainingLength = 0
        self.repeat = False

    def getNextSong(self):
        if self._remainingLength == 0 and self.repeat == False:
            return False
        elif self._remainingLength == 0 and self.repeat == True:
            if len(self._queue) > 0:
                self._playerHead = -1
                self._remainingLength = self._queueLength
            else:
                return False
        self._playerHead += 1
        self._remainingLength -=1
        return self._queue[self._playerHead]

    def getPreviousSong(self):
        if self._remainingLength <= 0:
            if self._queueLength > 0:
                self._playerHead = self._queueLength - 1
                self._remainingLength = 0
                return self._queue[self._playerHead]
            return False
         
        self._playerHead -= 1
        self._remainingLength +=1
        return self._queue[self._playerHead]
    
    def appendSong(self,songData):
        self._queue.append(songData)
        self._remainingLength += 1
        self._queueLength += 1

    def addNextSong(self,songData):
        self._remainingLength += 1
        self._queueLength += 1
        pos = self._playerHead + 1
        self._queue = self._queue[:pos] + [songData] + self._queue[pos:]

    def removeNextSong(self):
        pos = self._playerHead + 1
        self._queue = self._queue[:pos-1] + self._queue[pos:]
        self._remainingLength =- 1
        self._queueLength -=1

    def removeSongPosition(self,position):
        self._queue = self._queue[:position-1] + self._queue[position:]
        self._queueLength -=1
        if position >= self._playerHead:
            self._remainingLength -=1

    def moveSong(self,originalPos,newPos):
        songData = self._queue[originalPos]
        tempQueue = self._queue[:originalPos-1] + self._queue[originalPos:]
        self._queue = tempQueue[:newPos] + [songData] + tempQueue[newPos:]

    def clear(self):
        self._queue = []
        self._playerHead = -1
        self._queueLength = 0
        self._remainingLength = 0

    def shuffle(self):
        random.shuffle(self._queue)
        self._remainingLength = self._queueLength
        self._playerHead = -1

    def enableRepeat(self):
        self.repeat = True

    def disableRepeat(self):
        self.repeat = False
    def outputRawList(self):
        print(self._queue)
        print("head:",self._playerHead)
        print("remaining Length:", self._remainingLength)