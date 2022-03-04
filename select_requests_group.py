import sqlalchemy

engine = sqlalchemy.create_engine(
    'postgresql+psycopg2://py48user1:12345@localhost:5432/py48db1'
)
connection = engine.connect()
print(engine)

# количество исполнителей в каждом жанре;
def select_request_1():
    sel = connection.execute("""
    SELECT name,  COUNT(performer_id) FROM genres g
    JOIN genreperformer gp ON g.id = gp.genre_id
    GROUP BY name;
    """).fetchall()
    print(sel)

# количество треков, вошедших в альбомы 2019-2020 годов;
def select_request_2():
    sel = connection.execute("""
    SELECT a.name,  COUNT(t.id) FROM albums a
    JOIN tracks t ON a.id = t.albums_id
    WHERE year_of_release BETWEEN '2019-01-01' AND '2020-12-31'
    GROUP BY a.name;
    """).fetchall()
    print(sel)

# средняя продолжительность треков по каждому альбому;
def select_request_3():
    sel = connection.execute("""
    SELECT a.name,  ROUND(AVG(t.duration), 2) FROM albums a
    JOIN tracks t ON a.id = t.albums_id
    GROUP BY a.name;
    """).fetchall()
    print(sel)

# все исполнители, которые не выпустили альбомы в 2020 году;
def select_request_4():
    sel = connection.execute("""
    SELECT p.name FROM albums a
    JOIN performeralbum pa ON a.id = pa.album_id
    JOIN performers p ON pa.performer_id = p.id
    WHERE p.name NOT IN (
        SELECT p.name FROM albums a
        JOIN performeralbum pa ON a.id = pa.album_id
        JOIN performers p ON pa.performer_id = p.id
        WHERE year_of_release BETWEEN '2020-01-01' AND '2020-12-31')
    GROUP BY p.name;
    """).fetchall()
    print(sel)

# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
def select_request_5():
    sel = connection.execute("""
    SELECT c.name, p.name FROM performers p
    JOIN performeralbum pa ON p.id = pa.performer_id
    JOIN albums a ON pa.album_id = a.id
    JOIN tracks t ON a.id = t.albums_id
    JOIN collectiontrack ct ON t.id = ct.track_id
    JOIN collections c ON ct.collection_id = c.id
    WHERE p.name = 'Michael Jackson'
    GROUP BY c.name, p.name;
    """).fetchall()
    print(sel)

# название альбомов, в которых присутствуют исполнители более 1 жанра;
def select_request_6():
    sel = connection.execute("""
    SELECT a.name, p.name, COUNT(gp.genre_id) FROM genres g
    JOIN genreperformer gp ON g.id = gp.genre_id
    JOIN performers p ON gp.performer_id = p.id
    JOIN performeralbum pa ON p.id = pa.performer_id
    JOIN albums a ON pa.album_id = a.id
    GROUP BY a.name, p.name
    HAVING COUNT(gp.genre_id) > 1;
    """).fetchall()
    print(sel)

# наименование треков, которые не входят в сборники;
def select_request_7():
    sel = connection.execute("""
    SELECT name, id FROM tracks
    WHERE id NOT IN (
        SELECT track_id FROM collectiontrack
        WHERE id IS NOT NULL)
    GROUP BY name, id;
    """).fetchall()
    print(sel)

# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
def select_request_8():
    sel = connection.execute("""
    SELECT p.name,t.name, t.duration FROM tracks t
    JOIN albums a ON t.albums_id = a.id
    JOIN performeralbum pa ON a.id = pa.album_id
    JOIN performers p ON pa.performer_id = p.id
    WHERE duration = (
        SELECT MIN(duration) FROM tracks);
    """).fetchall()
    print(sel)

# название альбомов, содержащих наименьшее количество треков.
def select_request_9():
    sel = connection.execute("""
    SELECT a.name FROM tracks t
    JOIN albums a ON t.albums_id = a.id
    WHERE   (
        SELECT COUNT(t.albums_id) FROM tracks t
        JOIN albums a ON t.albums_id = a.id
        GROUP BY a.name)
    GROUP BY a.name;
    """).fetchall()
    print(sel)

select_request_1()
select_request_2()
select_request_3()
select_request_4()
select_request_5()
select_request_6()
select_request_7()
select_request_8()
select_request_9()
