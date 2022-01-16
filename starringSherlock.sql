alter table movies add column lexemesStarring tsvector;
update  movies set lexemesStarring = to_tsvector(Starring);
update movies set rank = ts_rank(lexemesStarring, plainto_tsquery(
(
select Starring from movies where url='sherlock-holmes'
)));
drop table if exists recommendationsbasedonsummaryfield;
CREATE table recommendationsbasedonsummaryfield as select url,rank from movies where rank > 0.05 order by rank desc limit 50;
\copy ( select * from recommendationsbasedonsummaryfield) to '/home/pi/RSL/top50starringSherlockhomles.csv' with csv;
