# Združevanje

```sql
SELECT stolpci, MIN(stolpec1), MAX(stolpec2), AVG(stolpec3)
FROM tabela
WHERE pogoj_za_vrstice
GROUP BY stolpec
HAVING pogoj_za_skupine (npr. MIN(stolpec) > 10)
ORDER BY urejevalni_kriterij
```

* `WHERE` se uporablja za **izbiro vrstic** pred združevanjem, `HAVING` se uporablja za **izbiro skupin** po združevanju

1. Povprečna ocena filmov iz leta 2000.
```sql
SELECT AVG(ocena)
FROM filmi
WHERE leto = 2000;
```

2. Povprečna ocena filmov za vsako leto.
```sql
SELECT leto, AVG(ocena)
FROM filmi
GROUP BY leto;
```

3. Povprečna ocena filmov daljših od 100 minut za vsako leto.
```sql
SELECT leto, AVG(ocena) AS povp_ocena, COUNT(*) AS st_filmov
FROM filmi
WHERE dolzina > 100
GROUP BY leto
```

4. Povprečna ocena filmov daljših od 100 minut za vsako leto, ko je bilo vsaj 5 filmov.
```sql
SELECT leto, AVG(ocena) AS povp_ocena, COUNT(*) AS st_filmov
FROM filmi
WHERE dolzina > 100
GROUP BY leto
HAVING st_filmov > 5;
```