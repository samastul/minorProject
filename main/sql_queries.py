from fileinput import close
import random
from . import models
import datetime 
from fpdf import FPDF

def questionEntry(subj, ques, marks, topic):
        
    models.questionBank.objects.create(marks=marks,ques=ques,subj=subj,chapter_number=topic)
  
def questionSelector(subj, topic_list, pattern):
    
    if pattern == "MST":

        result_list2 = []
        result_list4 = []
        result_list8 = []
        result_set2 = models.questionBank.objects.filter(subj=subj).filter(marks=2).filter(chapter_number__in=topic_list)
        result_set4 = models.questionBank.objects.filter(subj=subj).filter(marks=4).filter(chapter_number__in=topic_list)
        result_set8 = models.questionBank.objects.filter(subj=subj).filter(marks=8).filter(chapter_number__in=topic_list)
        for result in result_set2:
            result_list2.append(result.ques)
        for result in result_set4:
            result_list4.append(result.ques)
        for result in result_set8:
            result_list8.append(result.ques)

        paper = random.sample(result_list2, k=2) + random.sample(result_list4, k=3) + random.sample(result_list8, k=1)
        
    else:
        result_list2 = []
        result_list4 = []
        result_list8 = []
        result_set2 = models.questionBank.objects.filter(subj=subj).filter(marks=2).filter(chapter_number__in=topic_list)
        result_set4 = models.questionBank.objects.filter(subj=subj).filter(marks=4).filter(chapter_number__in=topic_list)
        result_set8 = models.questionBank.objects.filter(subj=subj).filter(marks=8).filter(chapter_number__in=topic_list)
        for result in result_set2:
            result_list2.append(result.ques)
        for result in result_set4:
            result_list4.append(result.ques)
        for result in result_set8:
            result_list8.append(result.ques)

        paper = random.sample(result_list2, k=8) + random.sample(result_list4, k=5) + random.sample(result_list8, k=2)
        

    current_date = datetime.date.today()
    current_time = datetime.datetime.now()

    datenow = current_date

    f = open("question_paper_{}_{}_{}.txt".format(subj,current_date,current_time.strftime("%H_%M_%S")),"w")
    #f = open("question_paper.txt","w")
    
    f.write("EXAM: ")
    f.write(pattern)
    f.write("\nSubject: ")
    f.write(subj)
    # f.write("\nDate:")
    # f.write(datenow)
    f.write("\n\n")
    #f.write(current_date)
    for i in range(len(paper)):
        f.write('Q{}:  {}\n'.format(i+1,paper[i]))
        
    f.close()
 
    pdf = FPDF() 
    pdf.add_page()
    pdf.set_font('Arial', size=15)

    f = open("question_paper_{}_{}_{}.txt".format(subj,current_date,current_time.strftime("%H_%M_%S")),"r")

    for x in f:
        pdf.multi_cell(180,10,txt=x,align='L')
    pdf.output("C:\\Users\\singh\\Documents\\question_paper_{}_{}_{}.pdf".format(subj,current_date,current_time.strftime("%H_%M_%S")))

    f.close()
