alter table movies add column lexemesSummary tsvector;
update  movies set lexemesSummary = to_tsvector(Summary);
update movies set rank = ts_rank(lexemesSummary, plainto_tsquery(
(
select Summary from movies where url='sherlock-holmes'
)));
drop table if exists recommendationsbasedonsummaryfield;
CREATE table recommendationsbasedonsummaryfield as select url,rank from movies where rank > 0.05 order by rank desc limit 50;
\copy ( select * from recommendationsbasedonsummaryfield) to '/home/pi/RSL/top50SummarySherlockholmes.csv' with csv;
