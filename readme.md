Python
Requires tqdm for progress bar in the terminal - or can remove this.

Rename NAPLAN PDF files from 'LASTNAME_FIRSTNAME.pdf' to 'code.pdf' where 'code' is their SCSA number (8 digit). Could alternatively use school code (4 digit) by changing code = student[1][3] to code = student[1][0]
Requires student_list.csv in the 'data_in' directory, with columns: 0 code (school code, optional), 1 first name, 2 surname, 3 scsa number.
