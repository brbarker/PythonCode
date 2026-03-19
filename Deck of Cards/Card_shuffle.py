import csv
hearts = ['h_1', 'h_2', 'h_3', 'h_4', 'h_5', 'h_6', 'h_7', 'h_8', 'h_9', 'h_10', 'h_J', 'h_Q', 'h_K']
spades = ['s_1', 's_2', 's_3', 's_4', 's_5', 's_6', 's_7', 's_8', 's_9', 's_10', 's_J', 's_Q', 's_K']
diamonds = ['d_1', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'd_8', 'd_9', 'd_10', 'd_J', 'd_Q', 'd_K']
clubs = ['c_1', 'c_2', 'c_3', 'c_4', 'c_5', 'c_6', 'c_7', 'c_8', 'c_9', 'c_10', 'c_J', 'c_Q', 'c_K']
full_deck = hearts+spades+diamonds+clubs
N = 52

def shuffle(pack_1, pack_2, pack_3, pack_4):
    preshuffle_1 = pack_1+pack_2
    preshuffle_2 = pack_3+pack_4
    preshuffle_1.reverse()
    preshuffle_2.reverse()
    to_shuffle = []
    
    for i in range(26):
        to_shuffle.append(preshuffle_1[i])
        to_shuffle.append(preshuffle_2[i])
        shuffled = to_shuffle
    return shuffled

def cut(after_shuffle):
    new_pack_1 = after_shuffle[0:13]
    new_pack_2 = after_shuffle[13:26]
    new_pack_3 = after_shuffle[26:39]
    new_pack_4 = after_shuffle[39:52]
    return [new_pack_1, new_pack_2, new_pack_3, new_pack_4]

shuffle_ = [None]*(N+1)
cut_ = [None]*(N+1)



with open('shuffles.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(1,N+1):
        
        if i == 1:
            print(full_deck.index('h_1')+1,full_deck.index('s_1')+1,full_deck.index('d_1')+1,full_deck.index('c_1')+1)
            shuffle_[i] = shuffle(hearts, spades, diamonds, clubs)
            shuffle_[i].reverse()
            cut_[i] = cut(shuffle_[i])
            #print('shuffle',[i],shuffle_[i])
            #print('cut',[i],cut_[i])
            #print(shuffle_[i].index('h_1')+1,shuffle_[i].index('c_K')+1)
            #print('')
        if i > 1:
            shuffle_[i] = shuffle(cut_[i-1][0],cut_[i-1][1],cut_[i-1][2],cut_[i-1][3])
            shuffle_[i].reverse()
            cut_[i] = cut(shuffle_[i])
            #print('shuffle',[i],shuffle_[i])
            #print('cut',[i],cut_[i])
            #print(shuffle_[i].index('h_1')+1,shuffle_[i].index('c_K')+1)
            #print('')
            if shuffle_[i] == full_deck:
                print('They match after',[i],'shuffles.')
                print('')
        row_write = (shuffle_[i].index('h_1')+1,shuffle_[i].index('s_1')+1,shuffle_[i].index('d_1')+1,shuffle_[i].index('c_1')+1)
        writer.writerow(row_write)
