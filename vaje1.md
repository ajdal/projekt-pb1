# Osnovne poizvedbe s SELECT

Vsi filmi z oceno višjo od 8 in več kot 10.000 glasovi, ki se začnejo z besedo Boter:
```sql
SELECT naslov, ocena
FROM film
WHERE ocena > 8 AND glasovi > 10000 AND naslov LIKE 'Boter%'
ORDER BY ocena DESC, naslov;
```

Filmi z oceno zaokroženo na cela števila:
```sql
SELECT naslov, ROUND(ocena) AS 'zaokrozena_ocena'
FROM film
WHERE ocena > 8 AND glasovi > 10000
ORDER BY ocena DESC, naslov;
```

```sql
SELECT naslov, ROUND(ocena)
FROM film
WHERE ROUND(ocena) = (SELECT MIN(ROUND(ocena)) FROM film);
```