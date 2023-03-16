-- Script that lists all shows contained in the databaseand displays null for shows without genre.
SELECT s.title, g.genre_id FROM tv_shows AS s
  LEFT JOIN tv_show_genres AS g ON s.id = g.show_id
    ORDER BY s.title, g.genre_id;
