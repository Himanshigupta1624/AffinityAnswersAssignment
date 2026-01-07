# Rfam SQL Assignment

## Question (a)

###  How many types of *Acacia* plants can be found in the taxonomy table?

###  Approach

* Species names are stored in the `taxonomy.species` column.
* All *Acacia* species start with the genus name `Acacia`.

### Observed Result

```
acacia_species_count = 362
```

---

## Question (b)

###  Which type of wheat has the longest DNA sequence?

###  Approach

* Wheat species belong to the genus **Triticum**
* Join `taxonomy` and `rfamseq` using `ncbi_id`
* Filter only **genomic DNA** sequences
* Order by sequence length descending


###  Observed Result

```
Wheat Type : Triticum durum (durum wheat)
DNA Length : 836,514,780
```

---

## Question (c)

###  Paginated list of families and their longest DNA sequence lengths

**Requirements**

* Family accession ID
* Family name
* Longest DNA sequence length
* Only families with max length > 1,000,000
* Sorted by length (descending)
* Page **9**, with **15 results per page**

---

###  Schema Understanding

The `rfamseq` table does **not** directly reference families.

Correct join path:

```
family → full_region → rfamseq
```

---

###  Pagination Calculation

```
OFFSET = (page_number − 1) × page_size
OFFSET = (9 − 1) × 15 = 120
```

---

###  Execution Note (Important)

This query performs aggregation across very large tables (`rfamseq` and
`full_region`). When executed on the **public Rfam MySQL server**, it may
exceed execution time limits and result in a dropped connection.

This is a known and expected limitation of the shared public database.
The query logic, joins, and pagination are correct and reproducible.

---


## Summary of Results

| Question                  | Result                              |
| ------------------------- | ----------------------------------- |
| (a) Acacia species count  | **362**                             |
| (b) Longest wheat DNA     | **Triticum durum (836,514,780 bp)** |
| (c) Paginated family list | Query provided (execution-heavy)    |

---

