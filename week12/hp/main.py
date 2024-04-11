import pandas as pd
import re
import csv

# DataFrame: [movie, chapter,character, dialog]

if __name__ == "__main__":

    str_filter = "[\(\[\{].*?[\)\]\}]"
    character_names_map = {"James":"James Potter","Trelawney":"Sybill Trelawney","Kingsley":"Kingsley Shacklebolt","Narcissa":"Narcissa Malfoy","Dolores umbridge":"Dolores Umbridge","Umbridge":"Dolores Umbridge","Lily":"Lily Potter","Elphias doge":"Elphias Doge","Xenophilius lovegood":"Xenophilius Lovegood","Luna":"Luna Lovegood","Mrs. weasley":"Molly Weasley","Death eater":"Death Eater","Mundungus":"Mundungus Fletcher","Tonks":"Nymphadora Tonks","Bill":"Bill Weasley","Aunt petunia":"Petunia Dursley","Uncle vernon":"Vernon Dursley","Wormtail":"Peter Pettigrew","Bellatrix":"Bellatrix Lestrange","Thicknesse":"Pius Thicknesse","Yaxley":"Corban Yaxley","Mr. granger":"Mr. Granger","Mrs. granger":"Mrs. Granger","Scrimgeour":"Rufus Scrimgeour","Barty jr":"Bartemius Crouch Junior","Fleur":"Fleur Delacour","Nigel":"Nigel Wolpert","Viktor":"Viktor Krum","Rita":"Rita Skeeter","Mad-eye":"Alastor Moody","Severus":"Severus Snape","Igor":"Igor Karkaroff","Cho":"Cho Chang","Barty":"Bartemius Crouch","Cedric":"Cedric Diggory","Amos":"Amos Diggory", "Pettigrew":"Peter Pettigrew","Sirius":"Sirius Black",'Padma':"Padma Patil", 'Parvati':"Parvati Patil", 'Pansy':"Pansy Parkinson","Dean":"Dean Thomas", "Professor trelawney":"Sybill Trelawney", "Malfoy":"Draco Malfoy", "Lupin":"Remus Lupin", "Molly":"Molly Weasley", "Arthur":"Arthur Weasley","Fudge":"Cornelius Fudge","Marge":"Marge Dursley","Goyle":"Gregory Goyle","Colin":"Collin Creevey","Crabbe":"Vincent Crabbe","Professor McGonagall":"Minerva McGonagall","Lucius":"Lucius Malfoy", "Riddle":"Tom Riddle","Myrtle":"Moaning Myrtle","Madam Pomfrey":"Poppy Pomfrey","Professor Sprout":"Pomona Sprout","Lockhart":"Gilderoy Lockhart","Mr. Weasley":"Arthur Weasley",'Dumbledore': "Albus Dumbledore", "Flint": "Marcus Flint", 'McGonagall': "Minerva McGonagall", 'Hagrid': "Rubeus Hagrid", 'Petunia': "Petunia Dursley", 'Dudley': "Dudley Dursley", 'Vernon': "Vernon Dursley", 'Harry': "Harry Potter", 'Quirrell': "Quirinus Quirrell", 'Ollivander': "Garrick Ollivander", 'Mrs. Weasley': "Molly Weasley", 'George': "George Weasley", 'Fred': "Fred Weasley",
                           'Ginny': "Ginny Weasley", 'Ron': "Ron Weasley", 'Hermione': "Hermione Granger", 'Neville': "Neville Longbottom", 'Draco': "Draco Malfoy", 'Seamus': "Seamus Finnigan", 'Percy': "Percy Weasley", 'Nick': "Nearly Headless Nick", 'Snape': "Severus Snape", 'Hooch': "Rolanda Hooch", 'Filch': "Argus Filch", 'Oliver': "Oliver Wood", 'Flitwick': "Filius Flitwick", 'Lee': "Lee Jordan", 'Unseen Inhuman Voice': "Voldemort"}
    

    for i in range(1,9):
        filename=f"hp{i}"
        with open(f"scripts/{filename}.txt", encoding="utf8") as f:
            script_lines = list(map(str.strip, re.sub(
                str_filter, "", f.read()).splitlines()))
        movie = script_lines.pop(0)
        chapter, character, dialog = "", "", ""
        movie_data = []
        chapters = set()
        for i, line in enumerate(script_lines[:]):
            if not(line) or ("[" in line) or ("]" in line):
                continue
            # print(l.split(":")[0])
            elif ':' not in line:
                chapter = line
                chapters.add(chapter)
            else:
                characters, dialog = map(str.strip, line.split(':', 1))
                if characters == "All three":
                    characters = "Harry and Hermione and Ron"
                for character in characters.split(" and "):
                    if character in character_names_map:
                        movie_data.append({'movie': movie, 'chapter': chapter,
                                        'character': character_names_map[character], 'dialog': dialog})
                    else:
                        movie_data.append(
                            {'movie': movie, 'chapter': chapter, 'character': character, 'dialog': dialog})
        movie_df = pd.DataFrame(movie_data)
        movie_df.to_csv(f"datasets/{filename}.csv",
                        quoting=csv.QUOTE_ALL, index=False)

        # Check if missing chapter in script original text file
        # print(chapters-set(movie_df['chapter'].unique()))
        # print(movie_df.character.unique())
        # print(movie_df.head())
