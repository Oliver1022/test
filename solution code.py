def loadFilms():
    ''' load the films into a database from the file (films.txt) and return it'''
    filmList=[]
    for eachLine in originalFile:
        eachLine=eachLine.strip()
        filmList=filmList+[eachLine.split(",")]
    print(filmList)
    return filmList
    

def printFilm(films):
    '''list all the films in the database'''
    i=0
    while i < len(films):
        print("Film:",i+1,"\n",\
              "Film name:",films[i][0],"\n",\
              "Film director:",films[i][1],"\n",\
              "Film actors:",films[i][2],films[i][3])
        i=i+1

def addFilm(films):
    '''add a film to the database and print new list of films'''
    input_Film_name=input("Please input film name:")
    input_Film_director=input("Please input film director:")
    input_Film_actor1=input("Please iput film actor1:")
    input_Film_actor2=input("Please iput film actor2:")
    films_append=[input_Film_name,input_Film_director,input_Film_actor1,input_Film_actor2]
    films=films+[films_append]
    print(films)
    return films

def saveFilms(films):
    '''save the films in a database to a new file'''
    newfile=open("newfile.txt","w")
    i=0
    while i < len(films):
        newfile.write("{filmName},{filmdirector},{filmactor1},{filmactor2}\n".format(\
            filmName=films[i][0],filmdirector=films[i][1],filmactor1=films[i][2],filmactor2=films[i][3],k="\n"))
        i=i+1
    newfile.close()
        
    




originalFile=open("file.txt","w")
originalFile.write("\
The Shawshank Redemption,Frank Darabont,Tim Robbins,Morgan Freeman\n\
The Godfather,Francis Ford Coppola, Marlon Brando,Al Pacino\n\
The Dark Knight,Christopher Nolan,Christian Bale,Heath Ledger")
originalFile.close()
#create the original file

originalFile=open("file.txt")

films=loadFilms()
#print database

printFilm(films)
#print the list of all the films in the database

films=addFilm(films)
#add a film to the database and print new list of films


saveFilms(films)
# save the films in a database to a new file()

originalFile.close()
