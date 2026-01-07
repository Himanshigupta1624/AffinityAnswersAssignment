-- c) We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)
select f.rfam_acc as family_accession_id,
f.rfam_id as family_name, MAX(r.LENGTH) as max_dna_sequence_length
from family f 
join full_region fr on f.rfam_acc=fr.rfam_acc
join rfamseq r 
on fr.rfamseq_acc=r.rfamseq_acc
where r.mol_type="genomic DNA"
GROUP BY f.rfam_acc, f.rfam_id
HAVING MAX(r.LENGTH) > 1000000
ORDER BY max_dna_sequence_length DESC
LIMIT 15 OFFSET 120;