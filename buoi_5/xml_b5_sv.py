from lxml import etree

tree = etree.parse('sv.xml')

"""#### **Lấy tất cả sinh viên**"""

school = tree.xpath('//student')
for student in school:
  id = student.xpath('id/text()')[0]
  name = student.xpath('name/text()')[0]
  date = student.xpath('date/text()')[0]
  print(id, name, date)

"""#### **Liệt kê tên tất cả sinh viên**"""

list_name = tree.xpath('//student/name/text()')
print(list_name)

"""#### **Lấy tất cả id của sinh viên**"""

ids = tree.xpath('//student/id/text()')
print(ids)

"""#### **Lấy ngày sinh của sinh viên có id = "SV01"**"""

student_01_dob = tree.xpath("//student[id='SV01']/date/text()")[0]
print(student_01_dob)

"""#### **Lấy các khóa học**"""

course = tree.xpath('//enrollment/course/text()')
print(course)

"""#### **Lấy toàn bộ thông tin của sinh viên đầu tiên**"""

sv01_info = tree.xpath('//student[1]')
print(etree.tostring(sv01_info[0], pretty_print=True, encoding="unicode"))

"""#### **Lấy mã sinh viên đăng ký khóa học "Vatly203"**"""

registered_students = tree.xpath('//enrollment/course[text()="Vatly203"]/../studentRef/text()')
print(registered_students)

"""#### **Lấy tên sinh viên học môn "Toan101"**"""

toan101_names = tree.xpath("//student[id = //enrollment[course='Toan101']/studentRef]/name/text()")
print(toan101_names)

"""#### **Lấy tên sinh viên học môn "Vatly203"**"""

vatly203_names = tree.xpath("//student[id = //enrollment[course='Vatly203']/studentRef]/name/text()")
print(vatly203_names)

"""#### **Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997**"""

year1997 = tree.xpath("//student[date[starts-with(.,'1997')]]/name/text() | //student[date[starts-with(.,'1997')]]/date/text()")
print(year1997)

"""#### **Lấy tên của các sinh viên có ngày sinh trước năm 1998**"""

names_of_students = tree.xpath("//student[date[substring(.,1,4) < '1998']]/name/text()")
print(names_of_students)

"""#### **Đếm tổng số sinh viên**"""

total_student = tree.xpath('count(//student)')
print(total_student)

"""#### **Thêm vào file XML thông tin 2 sinh viên và viết câu xpath: Lấy tất cả sinh viên chưa đăng ký môn nào.**"""

register_yet = tree.xpath("//student[not(id = //enrollment/studentRef)]/name/text()")
print(register_yet)

"""#### **Lấy phần tử `<date>` anh em ngay sau `<name>` của SV01**"""

date_sibling_after_sv01 = tree.xpath("//student[id='SV01']/name/following-sibling::date/text()")
print(date_sibling_after_sv01)

"""#### **Lấy phần tử `<id>` anh em ngay trước `<name>` của SV02**"""

id_sibling_before_sv02 = tree.xpath("//student[id='SV02']/name/preceding-sibling::id/text()")
print(id_sibling_before_sv02)

"""#### **Lấy toàn bộ node `<course>` trong cùng một `<enrollment>` với `studentRef='SV03`'**"""

course_enroll_sv03 = tree.xpath("//enrollment[studentRef='SV03']/course")
print(etree.tostring(course_enroll_sv03[0], pretty_print=True, encoding="unicode"))

"""#### **Lấy sinh viên có họ là “Trần”**"""

firstname_is_tran = tree.xpath("//student[name[starts-with(.,'Trần')]]/name/text()")
print(firstname_is_tran)

"""#### **Lấy năm sinh của sinh viên SV01**"""

sv01_year = tree.xpath('substring(//student[id="SV01"]/date/text(), 1, 4)')
print(sv01_year)