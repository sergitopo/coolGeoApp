

COPY paystats(amount, p_date, p_age, p_gender, postal_code_id, id)
FROM '/tmp/data/paystats.csv'
DELIMITER ','
CSV HEADER;

COPY postal_codes(the_geom, code, postal_code_id)
FROM '/tmp/data/postal_codes.csv'
DELIMITER ','
CSV HEADER;
