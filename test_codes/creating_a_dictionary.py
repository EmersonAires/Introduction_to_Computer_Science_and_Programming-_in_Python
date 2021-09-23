def lyrics_to_frequencies(lyrics):
    myDict = {}

    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

#lyrics_thogetter = "One thing, I don't know why It doesn't even matter how hard you try Keep that in mind, I designed this rhyme To explain in due time (all I know)Time is a valuable thing Watch it fly by as the pendulum swings Watch it count down to the end of the day The clock ticks life away, it's so unreal (it's so unreal)"

#lyrics = lyrics_thogetter.split()


#print(lyrics_to_frequencies(lyrics))
