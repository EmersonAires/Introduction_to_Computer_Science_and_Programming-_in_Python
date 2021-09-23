import creating_a_dictionary

def most_common_words(freqs):

    values = freqs.values()
    best = max(values)
    words = []

    for k in freqs:
        if freqs[k] == best:
            words.append(k)
            
    return (words, best)
    
  

lyrics_thogetter = "One thing, I don't know why It doesn't even matter how hard you try Keep that in mind, I designed this rhyme To explain in due time (all I know)Time is a valuable thing Watch it fly by as the pendulum swings Watch it count down to the end of the day The clock ticks life away, it's so unreal (it's so unreal)"

lyrics = lyrics_thogetter.split()

most_common_words(creating_a_dictionary.lyrics_to_frequencies(lyrics))