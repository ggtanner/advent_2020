homework = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\18dec_input.txt","r")
problems = homework.readlines()

for problem in problems:
    problem_list = list(problem)
    sub_problems = []
    #find paranethisis
    open_para  = [idx for idx, element in enumerate(problem_list) if element == "("]
    close_para = [idx for idx, element in enumerate(problem_list) if element == ")"]
    
    print(open_para)
    print(close_para)