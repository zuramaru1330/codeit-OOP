class Student:

    def __init__(self, name, id, major):
        """ CheckPoint : 다른 자식 클래스로 넘겨주고 십다면 Argument 형식으로 선언하지 말고
            모클래스에서 사전에 Data type를 선언한뒤 자식 클래스로 Argument값을 넘겨주어야 한다.
            이러한 것을 'FIGURE'로 FLAG를 세워둘 것이다."""

        self.student_info = StudentInfo(name, id, major)  # Figure 1
        self.grades = []  # Figure 2
        self.gpa_manager = Grade(self.grades)  # Figure 2-1
        self.reportgrade = ReportGrade(self.student_info, self.gpa_manager)  # Figure 3 --> Tossing a class value


class StudentInfo:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major


class Grade:
    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)


class ReportGrade:

    def __init__(self, student_profile, gpa_manager):
        self.student_profile = student_profile
        self.gpa_manager = gpa_manager

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}" \
              .format(self.student_profile.name, self.student_profile.id, self.student_profile.major,
                      self.gpa_manager.get_average_gpa()))


# SOLID 기법 기반 Student Instance Define

younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.student_info.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# Add grade
younghoon.gpa_manager.add_grade(3.0)
younghoon.gpa_manager.add_grade(3.33)
younghoon.gpa_manager.add_grade(3.67)
younghoon.gpa_manager.add_grade(4.3)

# Print out Grades

younghoon.reportgrade.print_report_card()
