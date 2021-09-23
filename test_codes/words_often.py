import creating_a_dictionary as cDic
import most_common_words as mcw

def words_often(freqs, minTimes):
    result = []
    done = False

    while not done:
        temp = mcw.most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result



lyrics_thogetter = "One thing, I don't know why It doesn't even matter how hard you try Keep that in mind, I designed this rhyme To explain in due time (all I know)Time is a valuable thing Watch it fly by as the pendulum swings Watch it count down to the end of the day The clock ticks life away, it's so unreal (it's so unreal)"

lyrics = lyrics_thogetter.split()

words_often(cDic.lyrics_to_frequencies(lyrics), 2)