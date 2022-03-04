create table paystats (
    id integer,
    postal_code_id integer,
    p_gender varchar(1),
    p_age varchar(10),
    p_date date,
    amount real,
    PRIMARY KEY (id)
);

ALTER TABLE paystats ADD CONSTRAINT gender_check CHECK (p_gender IN ('F', 'M'));

create table postal_codes (
    postal_code_id integer,
    code integer,
    the_geom geometry(Geometry,4326),
    PRIMARY KEY (postal_code_id)
);

CREATE INDEX postal_codes_geom_idx ON postal_codes USING GIST(the_geom);

CREATE INDEX paystats_p_date ON paystats (p_date);

create or replace view paystats_by_gender_and_age_group as SELECT sum(amount) as sum,
       postal_code_id,
	   p_age,   
	   p_gender
FROM paystats
GROUP BY postal_code_id, p_gender, p_age order by 2, 3, 4;