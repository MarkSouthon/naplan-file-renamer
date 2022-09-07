import os, csv 
 
def main():
    stud_file = open('student_list.csv')
    stud_reader = csv.reader(stud_file)
    stud_list = list(stud_reader)
    # skip header row
    del stud_list[0]
    failed = open('data_out/fails.txt', 'w', newline='')
    lookup_dict = {}
    fail_list = []
    
    in_folder = 'data_in'
    out_folder = 'data_out'
    
        
    for student in (enumerate(stud_list)):
        # code is the SCSA number
        code = student[1][3] 
        firstname = student[1][1].upper()
        surname = student[1][2].upper()
        name = surname + '_' + firstname
        lookup_dict[name] = code
        
     
    for count, filename in enumerate(os.listdir(in_folder)):
        student_name = os.path.basename(filename)
        src =f"{in_folder}/{filename}"
        # remove '.pdf'
        student_name = student_name[:-4]
        try:
            new_filename = lookup_dict[student_name] + '.pdf'
            dst = f"{out_folder}/{new_filename}"
            os.rename(src, dst)
        except:
            if student_name != '.direc':
                fail_list.append(student_name)
                failed.write(student_name + "\n")
    
    print(f'Names of files unsuccessfully renamed: {fail_list}')
    
        
if __name__ == '__main__':
     
    # Calling main() function
    main()