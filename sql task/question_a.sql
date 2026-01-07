--  How many types of Acacia plants can be found in the taxonomy table of the dataset?
SELECT COUNT(*) from taxonomy as acacia_count
where species like 'Acacia %';

