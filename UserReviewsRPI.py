## Reading the csv file in Python.
import csv
with open('userReviews.csv', 'r', encoding= 'utf-8-sig') as userreviews:
    csv_reader = csv.reader(userreviews, delimiter=';')
    next(csv_reader, None)
    

## The variables that I have included in computing the below mentioned analysis. 
    author = []
    moviename = []
    score = []
    reviewerlist = []
    personal_score = 8.0
    moviename = 'avatar'

    
## The analysis that I would like to compute using the above mentioned variables.
    count = 0
    sum = 0
    avg = 0

    
## Computing and printing the count, sum and average for my favorite movie (Avatar) based on all reviews provided. 
    for i in csv_reader:
        if (i[0]) == 'avatar':
            sum+=float(i[1])
            count = count+1
            reviewerlist.append(i[2])
            print(reviewerlist)
            print("Scores given - " + (i[1]))
            print("The Sum - " + str(sum))
            print("The Count - " + str(count))
            
    avg = sum/count
    print(avg)



## Comparison of the above obtained value with my personal score on my favorite movie(Avatar).
avg = sum/count
print ("Average score - " + moviename + " : " + str(avg))
print ("Comparison to the personal score - " + str(personal_score-avg) + " (There is a 1.7333333333333334 difference between the personal score and the reviews' score.)")


## The list of Avatar Reviewers. 
print(moviename + " reviewers list: ")
print(reviewerlist)


## Reading the movies that have been watched by a reviewer that also watched my favorite movie. 

# Creating a final list variable to print out the final outputs. 
with open('userReviews.csv', 'r', encoding= 'utf-8-sig') as userreviews:
  filelist = []
  Finallist = []
  csv_reader = csv.reader(userreviews, delimiter=';')
  
# Computing the list of of reviewers, scores and movienames following the condition that the movie score is greater than the average score (greater than m). 
  for i in csv_reader:
        if(i[2]) in reviewerlist and float(i[1]) > float(avg):
            print('Reviewer: ' + i[2] + " Score: " + str(i[1]) +' Moviename: ' + str(i[0]))
            filelist.extend([i[0], i[1], i[2]])
            Finallist.extend([filelist])
            print(filelist)
            filelist = []

## Printing out the preferred variables (author, moviename and userscore) into a created csv file list based on the output. 
fields = [['Author', 'Moviename', 'Userscore']] 
file = open('Finaloutput.csv', 'w+', newline = '')
with file:
    write = csv.writer(file)
    write.writerow(fields)
    write.writerows(Finallist)