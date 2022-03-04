create table if not exists Genres (
	id serial primary key,
	name varchar(40) unique not null
);

create table if not exists Performers (
	id serial primary key,
	name varchar(40) not null
);

create table if not exists GenrePerformer(
	performer_id integer references Performers(id),
	genre_id integer references Genres(id),
	constraint gp primary key (performer_id, genre_id)
);

create table if not exists Albums (
	id serial primary key,
	name varchar(40) not null,
	album_release_year integer not null
);

create table if not exists PerformerAlbum (
	performer_id integer references Performers(id),
	album_id integer references Albums(id),
	constraint pa primary key (performer_id, album_id)
);

create table if not exists Tracks (
	id serial primary key,
	name varchar(40) not null,
	duration integer not null check(duration > 0),
	albums_id integer references Albums(id)
);

create table if not exists Collections (
	id serial primary key,
	name varchar(40) not null,
	collection_release_year integer not null	
);

create table if not exists CollectionTrack (
	track_id integer references Tracks(id),
	collection_id integer references Collections(id),
	constraint ct primary key (track_id, collection_id)
);