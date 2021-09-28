from Media import Media
import Film
import Series
import Clip
import Documentary
import pytube

def get_Media_information():
    n = input('Name: ')
    di = input('Director: ')
    i = float(input('IMDB Score: '))
    u = input('url: ')
    du = int(input('Duration in min: '))
    ca = input('Casts: ')
    return n, di, i, u, du, ca

def add_media():
    while True:
        print('1- Add Film ')
        print('2- Add Series ')
        print('3- Add Clip')
        print('4- Add Documentary')
        print('5- exit')

        choice = int(input('Please enter media want to add: '))
        if choice == 1:
            print('Please enter film information: ')
            inf = get_Media_information()
            ci = input('Cinema to release a movie: ')
            film = Film.Film('Film: ', inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], ci)
            MEDIAS.append(film)

        elif choice == 2:
            print('Please enter series information: ')
            inf = get_Media_information()
            sec = int(input('section: '))
            seo = int(input('season: '))
            series = Series.Series('Series: ', inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], sec , seo)
            MEDIAS.append(series)

        elif choice == 3:
            print('Please enter clip information: ')
            inf = get_Media_information()
            s = input('shortened from: ')
            clip = Clip.Clip('Clip: ', inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], s)
            MEDIAS.append(clip)

        elif choice == 4:
            print('Please enter documentary information: ')
            inf = get_Media_information()
            t = input('A truth taken from: ')
            documentary = Documentary.Documentary('Documentary: ', inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], t)
            MEDIAS.append(documentary)

        elif choice == 5:
            print('Medias add. ')
            break

        else:
            print('Wrong choice! Try again. ')

def edit_info_media(media , choice):
    if choice == 1:
        new_name = input('Enter new name: ')
        media.name = new_name

    elif choice == 2:
        new_director = input('Enter new director: ')
        media.director = new_director

    elif choice == 3:
        new_IMDB = float(input('Enter new IMDB Score: '))
        media.IMDB_Score = new_IMDB

    elif choice == 4:
        new_url = input('Enter new url: ')
        media.url = new_url

    elif choice == 5:
        new_duration = int('Enter new duration: ')
        media.duration = new_duration

    elif choice == 6:
        new_casts = input('Enter new casts: ')
        media.casts = new_casts

def edit_medias():
    name = input('Please enter name of madia that want to edit: ')
    f=0

    for i in range(len(MEDIAS)):
        if name == MEDIAS[i].name:
            print('Choose what info want to change: ')
            print('1- Edit name ')
            print('2- Edit director ')
            print('3- Edit IMDB score ')
            print('4- Edit url ')
            print('5- Edit duration ')
            print('6- Edit casts ')

            if type(MEDIAS[i]) == Film.Film:
                print('7- Edit cinema ')
                choice = int(input('Input your choice: '))
                edit_info_media(MEDIAS[i] , choice)
                if choice == 7:
                    new_cinema = input('Enter new cinema: ')
                    MEDIAS[i].cinema = new_cinema
            
            elif type(MEDIAS[i]) == Series.Series:
                print('7- section ')
                print('8- season ')
                choice = int(input('Input your choice: '))
                edit_info_media(MEDIAS[i] , choice)
                if choice == 7:
                    new_section = int(input('Enter new section: '))
                    MEDIAS[i].section = new_section
                elif choice == 8:
                    new_season = int(input('Enter new season: '))
                    MEDIAS[i].season = new_season

            elif type(MEDIAS[i]) == Clip.Clip:
                print('7- shortened' )
                choice = int(input('Input your choice: '))
                edit_info_media(MEDIAS[i] , choice)
                if choice == 7:
                    new_short = input('Enter new shortened: ')
                    MEDIAS[i].shortened = new_short
                
            elif type(MEDIAS[i]) == Documentary.Documentary:
                print('7- truth ')
                choice = int(input('Input your choice: '))
                edit_info_media(MEDIAS[i] , choice)
                if choice == 7:
                    new_truth = input('Enter new truth: ')
                    MEDIAS[i].truth = new_truth

            f=1

    if f == 0:
        print('This media not exist!!!')  

def search_info_media():
    name = input('Please enter name of madia that want to search: ')
    f=0

    for i in range(len(MEDIAS)):
        if name == MEDIAS[i].name:
            print(MEDIAS[i].show_info())
            f=1

    if f == 0:
        print('This media not exist!!!')       

def delete_media():
    name = input('Please enter name of madia that want to delete: ')
    f=0

    for i in range(len(MEDIAS)):
        if name == MEDIAS[i].name:
            del MEDIAS[i]
            f=1
            break
        
    if f == 0:
        print('This media not exist!!!') 

def download_media():
    name = input('Please enter name of madia that want to download: ')
    f=0

    for i in range(len(MEDIAS)):
        if name == MEDIAS[i].name:
            MEDIAS[i].download()
    if f == 0:
        print('This media not exist!!!') 

def search_time():
    a = int(input('Please enter time1 in min: '))
    b= int(input('Please enter time2 in min: '))

    for i in range(len(MEDIAS)):
        if a < MEDIAS[i].duration < b:
            print(MEDIAS[i].show_info())

def exit_program():
    new_medias = ''
    for i in range(len(MEDIAS)):
        name = MEDIAS[i].name
        director = MEDIAS[i].director
        IMDM_Score = str(MEDIAS[i].IMDB_Score)
        url = MEDIAS[i].url
        duration = str(MEDIAS[i].duration)
        casts = MEDIAS[i].casts

        media =  name + '-' + director + '-' + IMDM_Score + '-' + url + '-' \
                    + duration + '-' + casts + '-'

        if type(MEDIAS[i]) == Film.Film:
            cinema = MEDIAS[i].cinema
            if i == len(MEDIAS)-1 :
                new_media = 'Film: -' + media + cinema
            else:
                new_media = 'Film: -' + media + cinema + '\n'

        elif type(MEDIAS[i]) == Series.Series:
            section = str(MEDIAS[i].section)
            season = str(MEDIAS[i].season)
            if i == len(MEDIAS)-1 :
                new_media = 'Series: -' + media + section + '-' + season
            else:
                new_media = 'Series: -' + media + section + '-' + season + '\n'

        elif type(MEDIAS[i]) == Clip.Clip:
            shortened = MEDIAS[i].shortened
            if i == len(MEDIAS)-1 :
                new_media = 'Clip: -' + media + shortened
            else:
                new_media = 'Clip: -' + media + shortened + '\n'

        elif type(MEDIAS[i]) == Documentary.Documentary:
            truth = MEDIAS[i].truth
            if i == len(MEDIAS)-1 :
                new_media = 'Documentary: -' + media + truth
            else:
                new_media = 'Documentary: -' + media + truth + '\n'
        
        else:
            print('Medias list is empty!!!')

        new_medias += new_media

    file = open('Media_database.txt' , 'w')
    file = file.write(new_medias)
    exit()

def show_medias_list():
    for i in range(len(MEDIAS)):
        print(MEDIAS[i].show_info())   

def load():
    print('Loading... ')
    file = open('Media_database.txt' , 'r')
    file = file.read()
    medias_list = file.split('\n')
    for i in range(len(medias_list)):
        media = medias_list[i].split('-')
        if media[0] == 'Film: ':
            film = Film.Film(media[0], media[1], media[2], float(media[3]), media[4],
             int(media[5]), media[6], media[7])
            MEDIAS.append(film)
        elif media[0] == 'Series: ':
            series = Series.Series(media[0], media[1], media[2], float(media[3]), media[4],
             int(media[5]), media[6], int(media[7]), int(media[8]))
            MEDIAS.append(series)
        elif media[0] == 'Clip: ':
            clip = Clip.Clip(media[0], media[1], media[2], float(media[3]), media[4],
             int(media[5]), media[6], media[7])
            MEDIAS.append(clip)
        elif media[0] == 'Documentary: ':
            documentary = Documentary.Documentary(media[0], media[1], media[2], float(media[3]), media[4],
             int(media[5]), media[6], media[7])
            MEDIAS.append(documentary)
    print('Welcome')

def show_menu():
    print('1- Add media')
    print('2- Edit media')
    print('3- Search media')
    print('4- Delete media')
    print('5- Download media')
    print('6- Time search')
    print('7- Show Media list')
    print('8- Exit')

MEDIAS = []
load()

while True:
    show_menu()

    choice = int(input('Please enter your choice: '))
    if choice == 1:
        add_media()

    elif choice == 2:
        edit_medias()

    elif choice == 3:
        search_info_media()

    elif choice == 4:
        delete_media()

    elif choice == 5:
        download_media()

    elif choice == 6:
        search_time()

    elif choice == 7:
        show_medias_list()

    elif choice == 8:
        exit_program()

    else:
        print('Wrong choice! Try again. ')