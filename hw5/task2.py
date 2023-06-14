import datetime
from collections import defaultdict


class Homework:
    def __init__(self, text, days):
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self):
        current_time = datetime.datetime.now()
        return current_time <= self.created + self.deadline


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework, solution):
        if isinstance(homework, Homework):
            if homework.is_active():
                return HomeworkResult(self, homework, solution)
            else:
                raise DeadlineError('You are late')
        else:
            raise ValueError('You gave a non-Homework object')


class Teacher:
    homework_done = defaultdict(set)

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, days):
        return Homework(text, days)

    def check_homework(self, homework_result):
        if len(homework_result.solution) > 5:
            self.homework_done[homework_result.homework].add(homework_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework, None)


class HomeworkResult:
    def __init__(self, author, homework, solution):
        if isinstance(homework, Homework):
            self.homework = homework
            self.solution = solution
            self.author = author
            self.created = datetime.datetime.now()
        else:
            raise ValueError('You gave a non-Homework object')


class DeadlineError(Exception):
    pass


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()