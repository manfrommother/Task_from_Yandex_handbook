class Programmer():

    def __init__(self, name, grade, work_hours=0, salary=0, factor_salary_senior=0):
        self.name = name
        self.grade = grade
        self.work_hours = work_hours
        self.salary = salary
        self.factor_salary_senior = factor_salary_senior

    def __str__(self):
        return f'Programmer name:{self.name}, grade:{self.grade}'

    def work(self, time):
        self.time = time
        salary_range = {'Junior': 10,
                        'Middle': 15,
                        'Senior': 20}
        self.work_hours += time
        self.salary += salary_range[self.grade] * time

    def rise(self):
        if self.grade == 'Junior':
            self.grade = 'Middle'
        elif self.grade == 'Middle':
            self.grade = 'Senior'
        elif self.grade == 'Senior':
            self.factor_salary_senior += 1
            self.salary += self.time * self.factor_salary_senior

    def info(self):
        return f'{self.name} {self.work_hours}ч. {self.salary}тгр.'


test = Programmer('Ivan', 'junior')
print(test)