import sqlalchemy

engine = sqlalchemy.create_engine(
    'postgresql+psycopg2://py48user1:12345@localhost:5432/py48db1'
)
connection = engine.connect()


def insert_database_genres():
    list_genres = [
        'Rock', 'Hip hop',
        'Jazz', 'Pop music',
        'Classical music',
        'Chanson'
        ]
    col = 0
    for genre in list_genres:
        col += 1
        genre_v = f'\'{genre}\''
        connection.execute(
            'INSERT INTO genres \n'
            f'VALUES({col}, {genre_v});'
        )


def insert_database_performer():
    list_performer = [
        'I Prevail', 'Eminem',
        'Art Tatum', 'Michael Jackson',
        'Ludwig van Beethoven', 'Mikhail Krug',
        'Linkin Park', 'System of a Down', 'Пошлая Молли']
    col = 0
    for performer in list_performer:
        col += 1
        performer_v = f'\'{performer}\''
        connection.execute(
            'INSERT INTO performers \n'
            f'VALUES({col}, {performer_v});'
        )


def insert_database_collection():
    dict_year_name_collections = {
        'Classic': 2020,
        'Up-to-date jazz': 2018,
        'New pop music': 2020,
        'Piano chillout': 2014,
        'On the ridge': 2021,
        'Rap life': 2019,
        'danceXL': 2017,
        'ALT CTRL': 2021
        }
    col = 0
    for name, year in dict_year_name_collections.items():
        col += 1
        name_v = f'\'{name}\''
        connection.execute(
            'INSERT INTO collections \n'
            f'VALUES({col}, {name_v}, {year});'
        )


def insert_database_genre_performer():
    dict_id = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 1, 8: 1, 9: 1, 9: 4}
    for performer_id, genre_id in dict_id.items():
        connection.execute(
            'INSERT INTO genreperformer \n'
            f'VALUES({performer_id}, {genre_id});'
        )


def insert_database_albums():
    dict_albums = {
        'Lifelines': '2016-10-21',
        'Kamikaze': '2018-08-31',
        'More Than You Know': '2014-11-15',
        'Dangerous': '1991-11-26',
        'Beethoven Medley': '2020-10-5',
        'Калина-Малина': '2008-05-22',
        'One More Night': '2017-03-04',
        'Hypnotize': '2005-11-22',
        '8 способов как бросить...': '2017-02-24'
        }
    col = 0
    for name, date_release in dict_albums.items():
        col += 1
        name_v = f'\'{name}\''
        date_release_v = f'\'{date_release}\''
        connection.execute(
            'INSERT INTO albums \n'
            f'VALUES({col}, {name_v}, {date_release_v});'
        )


def insert_database_performer_album():
    dict_id = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
    for performer_id, album_id in dict_id.items():
        connection.execute(
            'INSERT INTO performeralbum \n'
            f'VALUES({performer_id}, {album_id});'
        )


def insert_database_tracks():
    dict_name_duration_id = {
        'My Heart I Surrender': [3, 1],
        'Normal': [4, 2],
        'Perdido': [5, 3],
        'Black or White': [4, 4],
        'Sonata No. 8 C Minor (Pathetique), Opus': [5, 5],
        'Жизнь Коли': [4, 6],
        'Invisible': [4, 7],
        'Lonely Day': [3, 8],
        'Супермаркет': [4, 9]
        }
    col = 0
    for name, list_dur_id in dict_name_duration_id.items():
        duration = list_dur_id[0]
        album_id = list_dur_id[1]
        col += 1
        name_v = f'\'{name}\''
        connection.execute(
            'INSERT INTO tracks \n'
            f'VALUES({col}, {name_v}, {duration}, {album_id});'
        )


def insert_database_collection_track():
    dict_id = {1: 7, 2: 6, 3: 2, 4: 3, 5: 4, 6: 1, 7: 8, 8: 8}
    for track_id, collection_id in dict_id.items():
        connection.execute(
            'INSERT INTO collectiontrack \n'
            f'VALUES({track_id}, {collection_id});'
        )


insert_database_genres()
insert_database_performer()
insert_database_collection()
insert_database_genre_performer()
insert_database_albums()
insert_database_performer_album()
insert_database_tracks()
insert_database_collection_track()
