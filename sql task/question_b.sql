-- Active: 1767701314033@@mysql-rfam-public.ebi.ac.uk@4497@Rfam
select t.species as wheat_type,r.length as dna_length
from taxonomy as t
join rfamseq as r  on t.ncbi_id=r.ncbi_id
where t.species like 'Triticum %' And mol_type="genomic DNA"
ORDER BY r.length DESC
LIMIT 1;
