import numpy as np
import random

georgian_first_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ',
                        'კლარა', 'სიმონ', 'ანზორ',
                        'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ',
                        'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა', 'ომარ', 'ტატიანა',
                        'ვიქტორ', 'კარინე',
                        'გუგული', 'კახა', 'როზა',
                        'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე',
                        'მინდია', 'ნათია', 'გულნარა', 'კახა',
                        'ელზა', 'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო',
                        'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']

georgian_last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია',
                       'კევლიშვილი', 'ბუჩუკური', 'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე',
                       'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა', 'ნაკაშიძე',
                       'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე',
                       'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე',
                       'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა',
                       'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე',
                       'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე',
                       'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']


def generate_student_name():
    first_name = random.choice(georgian_first_names)
    last_name = random.choice(georgian_last_names)
    return first_name + ' ' + last_name


student_names = [generate_student_name() for _ in range(100)]

scores = np.random.randint(1, 101, size=(100, 3))

average_scores = np.mean(scores, axis=1)

matrix = np.column_stack((np.array(student_names), scores, average_scores))


def highest_average_student(student_matrix):
    averages = student_matrix[:, -1]
    highest_average_index = np.argmax(averages)
    highest_average_student_name = student_matrix[highest_average_index][0]
    print(f"მოსწავლე ყველაზე მაღალი საშუალო ქულით: {highest_average_student_name}")


def highest_and_lowest_math_students(student_matrix):
    math_scores = student_matrix[:, 2]
    highest_math_index = np.argmax(math_scores)
    lowest_math_index = np.argmin(math_scores)

    highest_math_student_name = student_matrix[highest_math_index][0]
    lowest_math_student_name = student_matrix[lowest_math_index][0]

    print(f"მოსწავლე ყველაზე მაღალი ქულით მათემატიკაში: {highest_math_student_name}")
    print(f"მოსწავლე ყველაზე დაბალი ქულით მათემატიკაში: {lowest_math_student_name}")


def above_average_english_students(student_matrix):
    total_students = student_matrix.shape[0]
    english_scores_sum = 0
    for row in student_matrix:
        english_scores_sum += int(row[2])
    average_english_score = english_scores_sum / total_students

    print("\nმოსწავლეები საშუალოზე მაღალი ქულით ინგლისურში:")
    for row in student_matrix:
        if int(row[2]) > average_english_score:
            print(row[0])


def main():
    if __name__ == '__main__':
        highest_average_student(matrix)
        highest_and_lowest_math_students(matrix)
        above_average_english_students(matrix)


main()
