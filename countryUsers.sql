drop table country;
create table country(ts datetime, user_id TEXT, country_id TEXT, site_id TEXT);
--.output results.csv
.mode csv
.import SWE.csv country

.mode column
.header ON


-- site id with largest no. of users
select site_id, count(user_id) unique_user_id 
from country 
where country_id = 'BDV'
group by site_id
order by 2 desc
limit 1;

-- four users who visited a certain site more than 10 times. 
select user_id, site_id, count(*) num_visits
from country
where ts >= '2019-02-03 00:00:00' and
		ts <= '2019-02-04 23:59:59'
group by user_id, site_id
having count(*) > 10
order by user_id, site_id;

drop table user_ts;
create table user_ts(user_id TEXT, ts datetime);
INSERT INTO user_ts
select user_id, max(ts) as ts
from country
group by user_id;

-- top 3 sites
select site_id, count(t.user_id) as users
from country c left join user_ts t
	on c.user_id = t.user_id and
		c.ts = t.ts
group by site_id
order by 2 desc
limit 3;

drop table first_Last_site;
create table first_Last_site(user_id TEXT, fts datetime, lts datetime);
INSERT INTO first_Last_site
select user_id, min(ts), max(ts)
from country
group by user_id;

--number of users whose first/last visits are to the same website
select count(*)
from country c1, country c2, first_Last_site fts, first_Last_site lts 
where c1.user_id = c2.user_id and
	c1.user_id = fts.user_id and
	c2.user_id = lts.user_id and
	c1.ts = fts.fts and
	c2.ts = lts.lts and
	fts.fts <> lts.lts and
	c1.site_id = c2.site_id;
