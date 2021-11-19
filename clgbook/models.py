from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.files import ImageField


class CollageBaseManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError('Users must have there email')
        if not username:
            raise ValueError('Users must have there username.')

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CollegeAccount(AbstractBaseUser):
    username = models.CharField(verbose_name='College Name',max_length=500)
    email = models.EmailField(verbose_name='College Email',unique=True)
    phone = models.CharField(verbose_name='College Phone',unique=True, max_length=13)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CollageBaseManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perms):
        return self.is_admin

    def has_module_perms(self, label_app):
        return True



class COllegeInformationModel(models.Model):
    user = models.ForeignKey(CollegeAccount, on_delete=models.CASCADE)
    clg_image = models.ImageField(verbose_name='College Image', upload_to='college_img/%y')
    clg_university_img = models.ImageField(verbose_name='University Image', upload_to='university_img/%y')
    college_address = models.TextField(verbose_name='College Address')
    college_priciple = models.CharField(verbose_name='COllege Principle', max_length=300)
    college_HOD = models.CharField(verbose_name='COllege HOD', max_length=300)
    college_university = models.CharField(verbose_name='College University', max_length=300)
    date_upload = models.DateTimeField(verbose_name='Date Upload',auto_now_add=True)



DIVISION = (
    ('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),
)

COURSE_YEAR = (
    ('First Year','First Year'),
    ('Second Year','Second Year'),
    ('Third Year','Third Year'),
    ('Fourth Year','Fourth Year'),
)

GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)

COURSE = (
    ('BCA','BCA'),
    ('B-Tech','B-Tech'),
    ('Hotel Management','Hotel Management'),
    ('MCA','MCA'),
    ('M-Tech','M-Tech'),
    ('B-Com','B-Com'),
)

class StudentsModel(models.Model):
    user = models.ForeignKey(CollegeAccount, on_delete=models.CASCADE)
    student_image = models.ImageField(verbose_name='Student Image', upload_to='student_img/%y')
    student_name = models.CharField(verbose_name='Student Name', max_length=300)
    student_roll = models.PositiveIntegerField(verbose_name='Student Roll No.')
    student_age = models.PositiveIntegerField(verbose_name='Student Age')
    student_div = models.CharField(verbose_name='Student Division', choices=DIVISION,max_length=10)
    student_add = models.TextField(verbose_name='Student Address')
    student_course = models.CharField(verbose_name='Student Course Name', choices=COURSE, max_length=200)
    student_course_year = models.CharField(verbose_name='Student Course Year', choices=COURSE_YEAR, max_length=200)
    gender = models.CharField(verbose_name='Gender', choices=GENDER, max_length=200)
    student_fees = models.PositiveIntegerField(verbose_name='Student Fees')
    addmission_date = models.DateField(verbose_name='Addmission Date')


class FacultiesModel(models.Model):
    user = models.ForeignKey(CollegeAccount, on_delete=models.CASCADE)
    faculty_image = models.ImageField(verbose_name='Faculty Image', upload_to='faculty_img/%y')
    faculty_name = models.CharField(verbose_name='Faculty Name',max_length=300)
    faculty_age = models.PositiveIntegerField(verbose_name='Faculty Age')
    faculty_add = models.TextField(verbose_name='Faculty Address')
    faculty_teach_in_which_div = models.CharField(verbose_name='Faculty Teach In Which Div', choices=DIVISION,max_length=100)
    faculty_teach_in_which_class = models.CharField(verbose_name='Faculty Teach In Which Class', choices=COURSE,max_length=100)
    faculty_teach_in_which_year = models.CharField(verbose_name='Faculty Teach In Which Year Student',choices=COURSE_YEAR, max_length=100)
    gender = models.CharField(verbose_name='Gender', choices=GENDER, max_length=200)
    salary = models.PositiveIntegerField(verbose_name='Faculty Salary')
    joined_date = models.DateField(verbose_name='Joined Date')