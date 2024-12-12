CREATE OR REPLACE TABLE txn AS SELECT * FROM 'uncommitted/*.csv';

CREATE OR REPLACE TABLE charity AS SELECT * FROM 'registered_charities.csv';

CREATE OR REPLACE VIEW txn_charity_tax_exempt AS SELECT * FROM txn INNER JOIN charity USING (Name);

CREATE OR REPLACE VIEW txn_crunch AS
SELECT
    Date,
    COALESCE(Name, Description) AS Description,
    "Money In" AS "Paid In",
    -1 * "Money Out" AS "Paid Out"
FROM txn;
