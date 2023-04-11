-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);


SELECT COUNT(*) FROM users;

SELECT avg(balance) FROM users;

SELECT DISTINCT country FROM users;

SELECT country, avg(balance) FROM users
GROUP BY country;
--  지역별 평균 balance 구하기

-- SELECT AVG(age) ROM users WHERE age >= 30;

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
    );

-- 컬럼 순서도 써주는걸 권장
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');


UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid = 2;

DELETE FROM classmates
WHERE rowid=5;

SELECT rowid, *FROM classmates;

--이름에 '영'이 포함되는 모든 데이터 삭제하기
DELETE FROM classmates WHERE name LIKE '%영%';

--테이블의 모든 데이터 삭제하기
DELETE FROM classmates;