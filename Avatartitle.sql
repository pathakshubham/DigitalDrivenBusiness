alter table movies add column lexemestitle tsvector;
update  movies set lexemestitle = to_tsvector(title);
update movies set rank = ts_rank(lexemestitle, plainto_tsquery(
(
select title from movies where url='avatar'
)));
drop table if exists recommendationsbasedonsummaryfield;
CREATE table recommendationsbasedonsummaryfield as select url,rank from movies where rank > 0.05 order by rank desc limit 50;
\copy ( select * from recommendationsbasedonsummaryfield) to '/home/pi/RSL/top50titleAvatar.csv' with csv;
