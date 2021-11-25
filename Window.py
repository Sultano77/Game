import tkinter         # import de tkinter
import pandas as pd

def put_score(b , score_pseudo , name_pseudo):
    print(score_pseudo)
    df = pd.read_csv('assets/Classement.csv', header=0, sep=',')
    #test si le score est dans les 10 premiers:
    i_pseudo = 1
    b_one_time=False
    while i_pseudo <= df['Nom'].count() and i_pseudo<=10:
        if score_pseudo>=df.iloc[i_pseudo-1][1] and b_one_time==False:
            df.loc[df['Nom'].count()] = [name_pseudo,score_pseudo]
            b_one_time=True
        i_pseudo=i_pseudo+1
    #trie decroissant #charger dans le fichier
    df.sort_values(by = 'Score', ascending = False).to_csv('assets/Classement.csv', encoding='utf-8', index=False )

    #restitution sur l'interface user
    df = pd.read_csv('assets/Classement.csv', header=0, sep=',')
    i_pseudo = 1

    while i_pseudo <= df['Nom'].count() and i_pseudo<=10:
        print(df.iloc[i_pseudo - 1][0])
        l_pseudo = tkinter.Label(text=df.iloc[i_pseudo - 1][0])
        l_pseudo.grid(column=0, row=i_pseudo + 1)
        if score_pseudo > df.iloc[i_pseudo - 1][1]:
            l_pseudo = tkinter.Label(text=df.iloc[i_pseudo - 1][0])
            l_pseudo.grid(column=0, row=i_pseudo + 1)

        l_score = tkinter.Label(text=df.iloc[i_pseudo - 1][1])
        l_score.grid(column=1, row=i_pseudo + 1)
        i_pseudo = i_pseudo + 1
    b['state'] = tkinter.DISABLED


def MEP_Interface_Classement(score):
    root = tkinter.Tk ()   # création de la fenêtre principale

    l = tkinter.Label (text = "Pseudo (" + str(score) + ")")
    l.grid (column = 0, row = 0)

    s = tkinter.Entry ()
    s.grid (column = 1, row = 0)

    b = tkinter.Button (root,text = "Add Pseudo",command=lambda:put_score(b,score,s.get()))
    b.grid(column = 2, row = 0)

    l = tkinter.Label (text = "CLASSEMENT")
    l.grid (column = 1, row = 1)

    root.mainloop ()