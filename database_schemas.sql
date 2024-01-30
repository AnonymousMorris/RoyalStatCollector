CREATE TABLE IF NOT EXISTS fictions (
    id INT,
    title VARCHAR(100), 
    description VARCHAR(3000),
    rating DECIMAL(4, 2),
    chapters INT,
    retrieved_time DATETIME,
    url VARCHAR(200),
    followers INT, 
    pages INT,
    views INT,
    CONSTRAINT PK_Fictions PRIMARY KEY (id, retrieved_time)
);

CREATE TABLE IF NOT EXISTS rising_stars (
    id INT, 
    retrieved_time DATETIME,
    category VARCHAR(20),
    placement INT,
    CONSTRAINT PK_Rising_stars PRIMARY KEY (id, retrieved_time)
);

SELECT *
FROM fictions
WHERE EXISTS(
    SELECT 1
    FROM fictions AS t2
    WHERE fictions.id = t2.id
      AND fictions.title = t2.title
      AND fictions.description = t2.description
      AND fictions.rating = t2.rating
      AND fictions.chapters = t2.chapters
      AND fictions.retrieved_time > t2.retrieved_time
      AND fictions.url = t2.url
      AND fictions.followers = t2.followers
      AND fictions.pages = t2.pages
      AND fictions.views = t2.views
);